from django.db import models
from django.conf import settings
from stories.models import Story


class Comment(models.Model):
    text = models.TextField(
        max_length=500,
        help_text="Напишете вашия коментар тук..."
    )
    created_at = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    story = models.ForeignKey(
        Story,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    class Meta:
        verbose_name = "Коментар"
        verbose_name_plural = "Коментари"
        ordering = ['-created_at']

    def __str__(self):
        return f"Коментар от {self.author.username} към '{self.story.title}'"