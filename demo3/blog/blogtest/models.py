from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Classify(models.Model):
    """分类表"""
    designation = models.CharField(max_length=20)

    def __str__(self):
        return self.designation

    def des(self):
        return self.designation
    des.short_description = "文章分类"


class Article(models.Model):
    """文章表"""
    title = models.CharField(max_length=20)
    datetime = models.DateTimeField(auto_now_add=True)
    create = models.DateTimeField(auto_now=True)
    auth = models.ForeignKey(User, on_delete=models.CASCADE)
    hits = models.IntegerField()
    digest = models.TextField()
    classifyid = models.ForeignKey(Classify, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def title1(self):
        return self.title
    title.short_description = '文章标题'

    def pub_time(self):
        return self.datetime
    pub_time.short_description = "发表时间"

    def a(self):
        return self.auth
    a.short_description = '作者'

    def num(self):
        return self.hits
    num.short_description = '阅读次数'


class Lable(models.Model):
    """标签表"""
    tag_name = models.CharField(max_length=20)
    la = models.ManyToManyField(Article)

    def __str__(self):
        return self.tag_name

    def tag(self):
        return self.tag_name
    tag.short_description = "标签"
