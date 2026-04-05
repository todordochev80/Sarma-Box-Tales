from rest_framework import serializers
from .models import Story

class StorySerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    category = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Story
        fields = ['id', 'title', 'content', 'author', 'category', 'created_at']