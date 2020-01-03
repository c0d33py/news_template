from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView, ListView, DetailView
from .forms import CategoryForm, ArticleForm, HeadlineForm
from .models import Article


def Index(request):
    return render(request, 'news/index.html')



class ArticleCreate(CreateView):
    form_class = ArticleForm
    template_name = 'news/create_article.html'
    success_url = '/article/list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)



class ArticleList(ListView):
    model = Article
    template_name = 'news/list_article.html'
    queryset = Article.objects.all()



# class PostDetailView(DetailView):
#     template_name = 'news/post_detail.html'

#     def get_object(self):
#         id_ = self.kwargs.get("id")
#         return get_object_or_404(Post, id=id_)
