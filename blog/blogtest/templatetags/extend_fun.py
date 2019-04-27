from django import template
from ..models import Article
register = template.Library()


@register.simple_tag
def getdate():
    return Article.objects.all().dates('datetime', 'month', order='DESC')


@register.simple_tag
def latest_article(num=3):
    latest_post = Article.objects.all().order_by("-datetime")[:num]
    return latest_post
