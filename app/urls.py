from django.urls import path

from app.views import ArticleDetailView, CommentCreateView

urlpatterns = [
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('article/<int:pk>/add_comment/', CommentCreateView.as_view(), name='comment-create'),
]
