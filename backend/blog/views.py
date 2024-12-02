# views.py
from rest_framework import generics
from .models import BlogCategory, BlogPost, Comment
from .serializers import BlogCategorySerializer, BlogPostSerializer, CommentSerializer

# Для работы с категориями
class BlogCategoryListCreateView(generics.ListCreateAPIView):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer

class BlogCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BlogCategorySerializer

    def get_queryset(self):
        slug = self.kwargs['slug']
        return BlogCategory.objects.filter(slug=slug)
    
# Для работы с постами
class BlogPostListCreateView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class BlogPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

# Для работы с комментариями
class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
