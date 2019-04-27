from django.db import models

# Create your models here.


class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.btitle

    def title(self):
        return self.btitle
    title.short_description = '书籍名称'

    def pub_date(self):
        return self.bpub_date
    pub_date.short_description = '发布时间'


class AuthInfo(models.Model):
    aname = models.CharField(max_length=20)
    agender = models.CharField(max_length=20)
    aintro = models.CharField(max_length=100)
    aprice = models.IntegerField()
    bookid = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.aname

    def name(self):
        return self.aname
    name.short_description = '姓名'

    def gender(self):
        return self.agender
    gender.short_description = "性别"

    def intro(self):
        return self.aintro
    intro.short_description = '语录'

    def price(self):
        return self.aprice
    price.short_description = '价格'

