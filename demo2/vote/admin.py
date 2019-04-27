from django.contrib import admin
from .models import Question, VoteNum
# Register your models here.


class VoteInline(admin.StackedInline):
    model = VoteNum
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['que', ]
    list_filter = ['question', ]
    search_fields = ['question', ]
    inlines = [VoteInline, ]


class VoteNumAdmin(admin.ModelAdmin):
    list_display = ['opt', 'nums']
    list_filter = ['option', 'num']
    search_fields = ['option', 'num']


admin.site.register(Question, QuestionAdmin)
admin.site.register(VoteNum, VoteNumAdmin)
