from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget
from embed_video.admin import AdminVideoMixin
from . models import Article, Category, Headline, LiveST


# Register your models here.


admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Headline)


class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass
admin.site.register(LiveST, MyModelAdmin)
