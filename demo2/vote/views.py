from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, VoteNum

# Create your views here.
"""
这是注释
"""


def index(request):
    question = Question.objects.all()
    return render(request, 'vote/index.html', {'question': question})


def poll(request, num):
    que = Question.objects.get(pk=num)
    result = Question.objects.get(pk=num).votenum_set.all()
    return render(request, 'vote/poll.html', {'poll': result, 'que': que})


def detail(request, id):
    try:
        info = Question.objects.get(pk=id)
        vote = info.votenum_set.get(pk=request.POST['poll'])
        vote.num += 1
        vote.save()
        return HttpResponseRedirect('/vote/info/'+id+'/',)
    except:
        return HttpResponseRedirect('/vote/poll/'+str(id)+'/')


def info(request, id):
    info = Question.objects.get(pk=id)
    return render(request, 'vote/detail.html', {'info': info})


def all(request):
    allinfo = Question.objects.all()
    return render(request, 'vote/alldetail.html', {'all': allinfo})


def add(request):
    return render(request, 'vote/addquestion.html')


def writeque(request):
    request = request.POST['question']
    q1 = Question()
    q1.question = request
    q1.save()
    return HttpResponseRedirect('/vote/')


def dropque(request, num):
    Question.objects.get(pk=num).delete()
    return HttpResponseRedirect('/vote/')


def edit(request, id):
    que = Question.objects.get(pk=id)
    return render(request, 'vote/addquestion.html', {'que': que, 'choice': 1})


def editsave(request, id):
    question = request.POST['question']
    q = Question.objects.get(pk=id)
    q.question = question
    q.save()
    return HttpResponseRedirect('/vote/')


def addoption(request, id):
    return render(request, 'vote/addoption.html', {'vote': id})


def writeoption(request, id):
    option = request.POST['option']
    q = Question.objects.get(pk=id)
    vote = VoteNum()
    vote.option = option
    vote.num = 0
    vote.qid = q
    vote.save()
    return HttpResponseRedirect('/vote/poll/'+id+'/')
