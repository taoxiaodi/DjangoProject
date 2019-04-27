from django.shortcuts import render, get_object_or_404, reverse, redirect
from blogtest.models import Article
from .forms import CommentForm
from django.http.response import HttpResponse

# Create your views here.


def discuss(request, num):
    post = get_object_or_404(Article, pk=num)
    if request.method == 'POST':
        comment = CommentForm(request.POST)

        if comment.is_valid():
            comment = comment.save(commit=False)
            comment.article_id = post
            comment.save()
            return redirect(reverse('blogtest:detail', args=(num, )))
        else:
            return HttpResponse('评论失败')
    return HttpResponse('评论失败了哦！！！')
