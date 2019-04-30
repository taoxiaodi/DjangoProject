from django.db import models
from tinymce.models import HTMLField
# Create your models here.


class Book(models.Model):
    book = models.CharField(primary_key=True, max_length=20)
    title = models.CharField(max_length=20)
    pub_date = models.DateTimeField(auto_now_add=True)
    auth = models.CharField(max_length=20)
    # 出版社
    press = models.CharField(max_length=20)


class Student(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    college = models.CharField(blank=True, null=True, max_length=20)
    num = models.CharField(blank=True, null=True, max_length=20)
    email = models.EmailField(blank=True, null=True, max_length=20)
    is_active = models.BooleanField(default=False)


class Borrows(models.Model):
    user_name = models.CharField(max_length=20)
    book_id = models.CharField(max_length=20)
    date_borrow = models.DateTimeField(auto_now_add=True)
    date_return = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)


class HotPic(models.Model):
    name = models.CharField(max_length=20)
    pic = models.ImageField(upload_to='hotpic')
    index = models.SmallIntegerField(max_length=20)

    def __str__(self):
        return self.name


class TextInfo(models.Model):
    title = models.CharField(max_length=20)
    content = HTMLField()

    def __str__(self):
        return self.title
