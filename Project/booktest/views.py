from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import BookInfo, HeroInfo
from django.template import loader

# Create your views here.


def index(request):
    # # 加载模板
    # indextem = loader.get_template('booktest/index.html')
    # cont = {'username': 'tao'}
    # # 渲染模板
    # result = indextem.render(cont)
    # # 返回模板
    # return HttpResponse(result)
    return render(request, 'booktest/index.html', {'username': "首页"})


def list(request):
    # return HttpResponse('列表页')
    bl = BookInfo.objects.all()
    return render(request, 'booktest/list.html', {'booklist': bl})


def detail(request, num):
    try:
        result = BookInfo.objects.get(pk=num)
        # return HttpResponse(str(result))
        return render(request, 'booktest/detail.html', {'book': result})
    except:
        print("该书尚未上架")


def delete(request, num):
    try:
        BookInfo.objects.get(pk=num).delete()
        return HttpResponseRedirect('/booktest/list')
    except:
        return HttpResponse('删除失败')


def add(request, bookid):
    print(bookid)
    return render(request, 'booktest/add.html', {'bookid': bookid})


def addhero(request, num):
    hname = request.POST['name']
    hcontent = request.POST['hcontent']

    b = BookInfo.objects.get(pk=num)

    h1 = HeroInfo()
    h1.hname = hname
    h1.hgender = True
    h1.hcontent= hcontent
    h1.bookid = b
    h1.save()
    return HttpResponseRedirect('/booktest/detail/'+str(num)+'/')


def addbook(request):
    return render(request, 'booktest/addbook.html')


def bookname(request):
    book = request.POST['book']
    b1 = BookInfo()
    b1.btitle = book
    b1.save()
    return HttpResponseRedirect('/booktest/list/')


def editbook(request, id):
    bookname = BookInfo.objects.get(pk=id)
    return render(request, 'booktest/editbook.html', {"bookname": bookname, 'bookid': id})


def editname(request, id):
    book = request.POST['book']
    b1 = BookInfo.objects.get(pk=id)
    print(b1)
    b1.btitle = book
    b1.save()
    return HttpResponseRedirect('/booktest/list/')


def edithero(request, id):
    hero = HeroInfo.objects.all().get(pk=id)
    return render(request, 'booktest/edithero.html', {'hero': hero})


def editheroinfo(request, id):

    heroname = request.POST['hero']
    heroskill = request.POST['skill']
    hero = HeroInfo.objects.all().get(pk=id)
    bookid = HeroInfo.objects.get(pk=id).bookid.id
    hero.hname = heroname
    hero.hgender = True
    hero.hcontent = heroskill
    hero.save()

    return HttpResponseRedirect('/booktest/detail/'+str(bookid)+'/')


def drophero(request, id):
    bookid = HeroInfo.objects.get(pk=id).bookid.id
    HeroInfo.objects.get(pk=id).delete()
    return HttpResponseRedirect('/booktest/detail/'+str(bookid)+'/')





"""
绑定视图函数和路由
"""