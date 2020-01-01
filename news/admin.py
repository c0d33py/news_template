from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget
from . models import Article, Category, Headline, LiveST


# Register your models here.


admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Headline)
admin.site.register(LiveST)
