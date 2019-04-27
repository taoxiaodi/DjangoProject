from django.contrib import admin
from .models import BookInfo, AuthInfo
# Register your models here.


class AuthInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'gender', 'price', 'intro']
    list_filter = ['aname', 'agender', 'aprice']
    search_fields = ['aname', 'agender', 'aprice']
    list_per_page = 5


class BookInline(admin.StackedInline):
    model = AuthInfo
    extra = 1


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['title', 'pub_date']
    list_filter = ['btitle', 'bpub_date']
    search_fields = ['btitle']
    list_per_page = 5

    inlines = [BookInline]


admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(AuthInfo, AuthInfoAdmin)
