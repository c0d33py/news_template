from django.urls import path
from .views import ArticleCreate, ArticleList


urlpatterns = [
    path('', ArticleCreate.as_view(), name='article-create'),
    path('news/list/', ArticleList.as_view(), name='artcle-list'),
    # path('post/<int:id>/', PostDetailView.as_view(), name='post-detail'),
]
