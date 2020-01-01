from django import forms
from . models import Category, Article, Headline


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields  = ['name', 
                   'disc', 
                   'slug'
                   ]



class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title',
                  'content', 
                  'categories',
                  'file_upload', 
                  'thumbnail', 
                  'status'
                  ]




class HeadlineForm(forms.ModelForm):
    class Meta:
        model = Headline
        fields = ['breaking', 
                  'head_status'
                  ]
