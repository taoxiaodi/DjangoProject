from django.db import models

# Create your models here.


class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.btitle

    def title(self):
        return self.btitle
    title.short_description = '书名'

    def time(self):
        return self.bpub_date
    time.short_description = '发布时间'


class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=50)
    bookid = models.ForeignKey(to='BookInfo', on_delete=models.CASCADE)

    def __str__(self):
        return self.hname

    def name(self):
        return self.hname
    name.short_description = '姓名'

    def gender(self):
        return self.hgender
    gender.short_description = '性别'

    def content(self):
        return self.hcontent
    content.short_description = '技能'

