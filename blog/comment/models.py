from django.db import models
from blogtest.models import Article


# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    creat_time = models.DateTimeField(auto_now_add=True)
    discuss = models.TextField()
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
