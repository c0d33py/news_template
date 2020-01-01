from django.urls import path
from .views import ArticleCreate


urlpatterns = [
    path('', ArticleCreate.as_view(), name='article-create'),
    # path('post/list/', PostListView.as_view(), name='post-list'),
    # path('post/<int:id>/', PostDetailView.as_view(), name='post-detail'),
]
