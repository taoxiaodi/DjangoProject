from django.shortcuts import render, reverse, redirect
from django.http.response import HttpResponse, HttpResponseRedirect
# Create your views here.
from .models import Article, Lable, Classify


def index(request):
    article = Article.objects.all()
    lable = Lable.objects.all()
    classify = Classify.objects.all()
    lastarticle = Article.objects.all().order_by('-datetime')[:3]
    content = {
        'article': article,
        'lable': lable,
        'classify': classify,
        'lastarticle': lastarticle,
    }
    return render(request, 'article_text.txt/blog.html', content)


def lable(request, id):
    label = Lable.objects.all()
    classify = Classify.objects.all()
    tag = Lable.objects.get(pk=id).la.all()
    lastarticle = Article.objects.all().order_by('-datetime')[:3]
    content = {
        'lable': label,
        "tag": tag,
        'classify': classify,
        'lastarticle': lastarticle,
        }
    return render(request, 'article_text.txt/lable.html', content)


def classify(request, id):
    aritcle = Classify.objects.get(pk=id)
    lable = Lable.objects.all()
    classify = Classify.objects.all()
    lastarticle = Article.objects.all().order_by('-datetime')[:3]
    content = {
        'lable': lable,
        'classify': classify,
        'article': aritcle,
        'lastarticle': lastarticle,
    }
    return render(request, 'article_text.txt/classify.html', content)


def detail(request, id):
    article = Article.objects.get(pk=id)
    article.hits += 1
    article.save()
    lable = Lable.objects.all()
    classify = Classify.objects.all()
    lastarticle = Article.objects.all().order_by('-datetime')[:3]
    content = {
        'lable': lable,
        'classify': classify,
        'article': article,
        'lastarticle': lastarticle,
        # 'comment': CommentForm()
    }
    return render(request, 'article_text.txt/detail.html', content)


def pigeonhole(request, id):
    article = Article.objects.filter(datetime__month=int(id)).all()
    lable = Lable.objects.all()
    classify = Classify.objects.all()
    lastarticle = Article.objects.all().order_by('-datetime')[:3]
    content = {
        'lable': lable,
        'classify': classify,
        'article': article,
        'lastarticle': lastarticle,
    }
    return render(request, 'article_text.txt/pigeonhole.html', content)


