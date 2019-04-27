from django.contrib import admin
from .models import Article, Classify, Lable
# Register your models here.


class LableInline(admin.StackedInline):
    model = Lable


class ClassifyInline(admin.StackedInline):
    model = Classify
    extra = 1


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title1', 'pub_time', 'a', 'num']
    list_filter = ['title', 'datetime', 'auth', 'hits']
    search_fields = ['title', 'datetime', 'auth', 'hits']
    list_per_page = 5
    inlines = [ClassifyInline, LableInline]


class ClassifyAdmin(admin.ModelAdmin):
    list_display = ['des']
    list_filter = ['designation']
    search_fields = ['designation']


class LableAdmin(admin.ModelAdmin):
    list_display = ['tag', ]
    list_filter = ['tag_name', ]
    search_fields = ['tag_name', ]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Classify, ClassifyAdmin)
admin.site.register(Lable, LableAdmin)
