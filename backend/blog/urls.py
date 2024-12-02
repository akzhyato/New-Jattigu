# urls.py
from django.urls import path
from .views import (
    BlogCategoryListCreateView,
    BlogCategoryDetailView,
    BlogPostListCreateView,
    BlogPostDetailView,
    CommentListCreateView,
    CommentDetailView,
)

urlpatterns = [
    path('categories/', BlogCategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<slug:slug>/', BlogCategoryDetailView.as_view(), name='category-detail'),
    path('posts/', BlogPostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', BlogPostDetailView.as_view(), name='post-detail'),
    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
]
