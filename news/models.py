from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from embed_video.fields import EmbedVideoField
from django.db import models
from django.urls import reverse

class LiveST(models.Model):
    title       = models.CharField(max_length=100)
    videos       = models.URLField(max_length=250, blank=True)
    video       = EmbedVideoField(blank=True)  # same like models.URLField()

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('post-detail', kwargs={'id': self.id})


class Category(models.Model):
    name            = models.CharField(max_length=100)
    disc            = models.TextField(max_length=500)
    slug            = models.SlugField(max_length=100)
    cat_date        = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    title           = models.CharField(max_length=100)
    categories      = models.ForeignKey('Category', default='1--', on_delete=models.CASCADE)
    file_upload     = models.FileField(upload_to='article/videos', blank=True, help_text='(optional)')
    thumbnail       = models.ImageField(upload_to='article/thumbnails', blank=True, help_text='(optional)')
    pub_date        = models.DateTimeField(auto_now_add=True)
    status          = models.BooleanField(default=True)
    content         = RichTextUploadingField(blank=True)
   

    def __str__(self):
        return self.title


class Headline(models.Model):
    breaking        = models.CharField(max_length=50)
    head_data       = models.DateTimeField(auto_now_add=True)
    head_status     = models.BooleanField(default=True)

    def __str__(self):
        return self.breaking
