from django.urls import path
from .views import ArticleCreate, ArticleList
from . import views


urlpatterns = [
    path('', views.Index, name='index'),
    path('create/', ArticleCreate.as_view(), name='article-create'),
    path('news/list/', ArticleList.as_view(), name='artcle-list'),
    # path('post/<int:id>/', PostDetailView.as_view(), name='post-detail'),
]
