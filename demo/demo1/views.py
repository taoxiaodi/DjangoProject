from django.shortcuts import render, redirect, reverse
from django.http.response import HttpResponseRedirect, HttpResponse
from .form import CustomForm
import datetime
# Create your views here.


def index(request):
    return render(request, 'demo1/index.html')


def list(request):
    return render(request, 'demo1/list.html')


def login(request):
    if request.method == 'GET':
        result = CustomForm()
        return render(request, 'demo1/login.html', {'result': result})
    elif request.method == 'POST':
        # form = CreatForm(request.POST)
        form = CustomForm(request.POST)
        form.save(commit=False)
        form.username = "123"

        # if form.is_valid():
             #  title = form.cleaned_data['title']
             #    time = form.cleaned_data['datetime']
             #    print(title, time)
        form.save()
        return HttpResponse('操作成功')
