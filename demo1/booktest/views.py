from django.shortcuts import render
from django.http import HttpResponse
from .models import BookInfo, AuthInfo
from django.template import loader
# Create your views here.


def index(request):
    # return HttpResponse("<h1>首页</h1>")
    # template = loader.get_template('booktest/index.html')
    # result = template.render()
    # print(result)
    # return HttpResponse(result)
    return render(request, 'booktest/index.html')


def book_list(request):
    # return HttpResponse("书籍列表")
    book = BookInfo.objects.all()
    return render(request, 'booktest/list.html', {'booklist': book})


def detail(request, num):
    # return HttpResponse('欢迎访问详情页'+num)
    info = BookInfo.objects.get(pk=num)
    return render(request, 'booktest/detail.html', {'info': info})
