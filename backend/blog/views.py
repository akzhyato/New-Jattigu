from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import BlogCategory, BlogPost, Comment
from .serializers import BlogCategorySerializer, BlogPostSerializer, CommentSerializer
from user.permissions import IsAdminUser, IsRegularUser

# Для работы с категориями
class BlogCategoryListCreateView(generics.ListCreateAPIView):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]  # Только для аутентифицированных администраторов

# Для работы с постами по категориям
class BlogPostCategoryView(generics.ListAPIView):
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticated, IsAdminUser | IsRegularUser]  # Для администраторов или обычных пользователей

    def get_queryset(self):
        slug = self.kwargs['slug']
        return BlogPost.objects.filter(category__slug=slug)

# Для работы с постами
class BlogPostListCreateView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]  # Только для аутентифицированных администраторов

    def perform_create(self, serializer):
        # Вы можете добавить дополнительную логику перед сохранением поста, если нужно
        serializer.save()

class BlogPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticated, IsAdminUser | IsRegularUser]  # Для администраторов или обычных пользователей

# Для работы с комментариями
class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAdminUser | IsRegularUser]  # Для администраторов или обычных пользователей

    def perform_create(self, serializer):
        # Устанавливаем автора как текущего пользователя
        serializer.save(author=self.request.user)

