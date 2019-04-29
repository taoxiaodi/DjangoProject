from django.contrib import admin
from .models import Student, Book, Borrows, HotPic, TextInfo
# Register your models here.

admin.site.register(Student)
admin.site.register(Book)
admin.site.register(Borrows)
admin.site.register(HotPic)
admin.site.register(TextInfo)
