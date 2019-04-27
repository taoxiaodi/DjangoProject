from django import template
from ..models import Article
register = template.Library()


@register.simple_tag
def gettag():
    return Article.objects.all().dates('datetime', 'month', order='DESC')

