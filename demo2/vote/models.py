from django.db import models

# Create your models here.


class Question(models.Model):
    question = models.CharField(max_length=50)

    def __str__(self):
        return self.question

    def que(self):
        return self.question
    que.short_description = '问题'


class VoteNum(models.Model):
    option = models.CharField(max_length=20)
    num = models.IntegerField()
    qid = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.option

    def opt(self):
        return self.option
    opt.short_description = '选项'

    def nums(self):
        return self.num
    nums.short_description = '票数'
