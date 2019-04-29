from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http.response import HttpResponse
from .models import Student, Book, Borrows, HotPic, TextInfo
from hashlib import sha1
import datetime
from django.core.mail import send_mail, send_mass_mail
from django.conf import settings
# Create your views here.


def index(request):
    """
    获取session为了防止没有session报错
    所以给个默认值None
    """
    pic = HotPic.objects.all().order_by('index')
    if request.session.get('username', None):
        return render(request, 'book/index.html', {'username': request.session.get('username', None), 'pics': pic, 'num':"0"})
    else:
        return render(request, 'book/index.html', {'username': None, "pics": pic})


def clear_info(request):
    """清除session"""
    del request.session['username']
    return redirect(reverse('book:index'))


def login(request):
    s1 = sha1()
    if request.method == "GET":
        return render(request, 'book/login.html')
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        s1.update(password.encode())
        password = s1.hexdigest()
        info = Student.objects.filter(username=username)[0]
        print(info.username, username)
        print(info.password, password)
        if info.username == username and info.password == password:
            request.session['username'] = username
            return redirect(reverse('book:index'))
        else:
            error = 'Invalid username'
            return render(request, 'book/login.html', {'error': error})


def register(request):
    user = Student()
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        confirm = request.POST['password2']
        college = request.POST['college']
        number = request.POST['number']
        email = request.POST['email']
        # 判断用户名是否已存在
        if len(Student.objects.filter(username=username)):
            error = "The username is already taken"
            return render(request, 'book/register.html', {'error': error})

        # 判断前后密码是否一致
        if password != confirm:
            error = " The two passwords do not match"
            return render(request, 'book/register.html', {'error': error})
        else:
            # sha1 加密密码
            s1 = sha1()
            s1.update(password.encode())
            password = s1.hexdigest()
            # 保存注册数据
            user.username = username
            user.password = password
            user.college = college
            user.num = number
            user.email = email
            user.save()

            # 注册发送邮箱验证

            return redirect(reverse('book:login'))
    return render(request, 'book/register.html')


def reader_info(request, name):
    user = Student.objects.filter(username=name)[0]
    content = {
        'user': user,
    }
    return render(request, 'book/reader_info.html', content)


def reader_modify(request):
    """用户修改信息"""
    reader = request.session.get('username', None)
    user = Student.objects.filter(username=reader)[0]
    content = {
        'user': user,
        'error': None,
    }
    return render(request, 'book/reader_modify.html', content)


def reader_save_modify(request):
    """用户修改信息之后从定向"""
    s1 = sha1()
    reader = request.session.get('username', None)
    user = get_object_or_404(Student, username=reader)
    # 判断用户名是否为空，如果为空进行Error提示
    if not request.POST['username']:
        content = {
            "error": "You have to input your name",
            'user': user,
        }
        return render(request, 'book/reader_modify.html', content)
    else:
        # 判断密码是否为空如果为空，则默认为不修改密码
        user.college = request.POST['college']
        user.num = request.POST['number']
        user.email = request.POST['email']
        user.username = request.POST['username']
        if request.POST['password']:
            # 修改密码的情况
            password = request.POST['password']
            s1.update(password.encode())
            password = s1.hexdigest()
            user.password = password
            user.save()
            del request.session['username']
            return redirect(reverse('book:login'))
        else:
            # 密码为空默认不修改的情况
            user.password = user.password
            user.save()
            del request.session['username']
            return redirect(reverse('book:login'))


def reader_query(request):
    if request.method == "GET":
        return render(request, 'book/reader_query.html')
    if request.method == "POST":
        result = request.POST['item']
        book_info = request.POST['query']
        # 判断是根据作者还是书名查询
        if result == 'title':
            book = Book.objects.filter(title=book_info)
            content = {
                'books': book,
            }

            return render(request, 'book/reader_query.html', content)
        elif result == 'auth':
            book = Book.objects.filter(auth=book_info)
            content = {
                "books": book,
            }

            return render(request, 'book/reader_query.html', content)
        else:
            return HttpResponse('查询失败')


def reader_book(request, num):
    book = Book.objects.get(pk=num)
    borrow = Borrows.objects.filter(book_id=num)
    if request.method == "GET":
        if borrow:
            content = {
                "book": book,
                "reader": borrow[0],
            }
            return render(request, 'book/reader_book.html', content)
        else:
            return render(request, 'book/reader_book.html', {'book': book})

    elif request.method == "POST":
        name = request.session.get('username', None)
        # 查看借阅记录的条数如果已存在记录，不在可以借阅
        if len(borrow) > 0:
            content = {
                'error': "你已经订阅!!!",
                'book': book,
                'reader': borrow[0],
            }
            return render(request, 'book/reader_book.html', content)
        # 保存借阅的记录
        borrow = Borrows()
        borrow.user_name = name
        borrow.book_id = num
        borrow.status = False
        borrow.save()
        date = Borrows.objects.filter(book_id=num)[0]
        date.date_borrow = datetime.datetime.now() + datetime.timedelta(days=30)
        date.save()

        return redirect(reverse('book:reader_book', args=(num,)))


def reader_history(request):
    name = request.session.get('username', None)
    history = Borrows.objects.filter(user_name=name).all()

    content = {
        'history': history,
    }
    return render(request, 'book/reader_history.html', content)


def up_load(request):
    if request.method == "GET":
        return render(request, 'book/up_load.html')
    elif request.method == "POST":
        name = request.POST['name']
        index = request.POST['index']
        pic = request.FILES['pic']
        img = HotPic(name=name, pic=pic, index=index)
        img.save()
        return redirect(reverse('book:index'))


def text(request, id):
    article = TextInfo.objects.get(pk=id)
    return render(request, 'book/text.html', {"texts": article})


def edit(request):
    if request.method == "GET":
        return render(request, 'book/edit.html',)
    elif request.method == "POST":
        title = request.POST['title']
        message = request.POST['message']
        msg = TextInfo(title=title, content=message)
        msg.save()
        return redirect(reverse('book:article_list'))


def article_list(request):
    article = TextInfo.objects.all()
    return render(request, 'book/list.html', {'articles': article, })


def mail(request):
    try:
        send_mail('Django发送邮件', '<a href="http://127.0.0.1:8000/book/">',
                  settings.DEFAULT_FROM_EMAIL,
                  ['1104056609@qq.com', ]
                  )
        return HttpResponse('发送成功')
    except:
        return HttpResponse('发送失败')
