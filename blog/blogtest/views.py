from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse
from .models import Article, Classify, Lable
from comment.forms import CommentForm
import markdown
from django.core.paginator import Paginator
# Create your views here.


def index(request):
    article = Article.objects.all()
    classify = Classify.objects.all()
    label = Lable.objects.all()

    paginato = Paginator(article, 2)
    pagenum = request.GET.get('page')
    pagenum = 1 if pagenum == None else pagenum
    print(pagenum)
    page = paginato.page(pagenum)
    content = {
        'article': page,
        'classify': classify,
        'label': label,
     }
    return render(request, 'blogtest/index.html', content)


def label(request, num):
    article = Lable.objects.get(pk=num).la.all()
    classify = Classify.objects.all()
    tag = Lable.objects.all()
    content = {
        'article': article,
        'classify': classify,
        'label': tag,
    }
    return render(request, 'blogtest/tag.html', content)


def classify(request, num):
    article = Classify.objects.get(pk=num)
    tag = Lable.objects.all()
    classify = Classify.objects.all()

    content = {
        'label': tag,
        'classify': classify,
        'article': article,
    }
    return render(request, 'blogtest/classify.html', content)


def pigeonhole(request, num):
    article = Article.objects.filter(datetime__month=int(num)).all()
    tag = Lable.objects.all()
    classify = Classify.objects.all()
    content = {
        'label': tag,
        'classify': classify,
        'article': article,
    }
    return render(request, 'blogtest/pigeonhole.html', content)


def detail(request, num):
    article = get_object_or_404(Article, pk=num)
    article.hits += 1
    article.save()
    tag = Lable.objects.all()
    classify = Classify.objects.all()

    # markdown的使用
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    article.digest = md.convert(article.digest)
    article.toc = md.toc
    content = {
        'label': tag,
        'classify': classify,
        'article': article,
        'post': CommentForm(),
    }
    return render(request, 'blogtest/detail.html', content)
