from django.contrib import admin
from .models import BookInfo,HeroInfo

# Register your models here.
# 注册模型


class HeroInfoInline(admin.StackedInline):
    model = HeroInfo
    extra = 1


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['title', 'time']
    inlines = [HeroInfoInline, ]


admin.site.register(BookInfo, BookInfoAdmin)


class HeroInfoAdmin(admin.ModelAdmin):
    # 后台显示的字段
    list_display = ['name', 'gender', 'content']
    # 过滤的字段
    list_filter = ['hname', 'hgender']
    # 搜索过滤
    search_fields = ['hname', 'hgender', 'hcontent']
    # 分页显示
    list_per_page = 4


admin.site.register(HeroInfo, HeroInfoAdmin)

"""
创建后台
"""
