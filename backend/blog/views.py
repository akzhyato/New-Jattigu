# views.py
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import BlogCategory, BlogPost, Comment
from .serializers import BlogCategorySerializer, BlogPostSerializer, CommentSerializer

# Для работы с категориями
class BlogCategoryListCreateView(generics.ListCreateAPIView):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer

# class BlogCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = BlogCategorySerializer

#     def get_queryset(self):
#         slug = self.kwargs['slug']
#         return BlogCategory.objects.filter(slug=slug)
    
class BlogPostCategoryView(generics.ListAPIView):
    serializer_class = BlogPostSerializer

    def get_queryset(self):
        slug = self.kwargs['slug']
        
        return BlogPost.objects.filter(category__slug=slug)

# Для работы с постами
class BlogPostListCreateView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def perform_create(self, serializer):
        # You can add any additional logic before saving the post if needed
        serializer.save()

class BlogPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

# Для работы с комментариями
class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Устанавливаем автора как текущего пользователя
        serializer.save(author=self.request.user)