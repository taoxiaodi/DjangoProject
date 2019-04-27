from django.contrib.syndication.views import Feed
from .models import Article
from django.shortcuts import reverse


class ArticleFeed(Feed):
    """
    进行网站包装成xml格式
    rss 可以把网站包装成xml格式
    可以通过rss聚合工具订阅
    """
    title = "文章"
    description = "摘要"
    link = '/'

    def items(self):
        return Article.objects.all()

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.digest

    def item_link(self, item):
        return reverse('blogtest:detail', args=(item.id, ))

