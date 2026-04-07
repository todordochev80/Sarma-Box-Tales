from django.db import models
from django.conf import settings

from categories.models import Category


class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class Story(models.Model):


    title = models.CharField(max_length=100, help_text="")
    content = models.TextField(help_text="")
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name='stories', blank=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_stories', blank=True)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='stories'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='stories'
    )

    def __str__(self):
        return f"{self.title} by {self.author.username}"

