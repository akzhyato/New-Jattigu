# serializers.py
from rest_framework import serializers
from .models import BlogCategory, BlogPost, Comment

class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = ['id', 'name', 'slug']

class BlogPostSerializer(serializers.ModelSerializer):
    category = BlogCategorySerializer()  # Вложенный сериализатор для категории
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'created_at', 'category', 'image', 'time_to_read']

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()  # Здесь можно использовать UserSerializer для подробного вывода информации
    class Meta:
        model = Comment
        fields = ['id', 'content', 'created_at', 'post', 'author']
