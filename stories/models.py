from django.db import models
from django.conf import settings


class Story(models.Model):
    CATEGORY_CHOICES = [
        ('Absurd', 'Абсурд'),
        ('Urban', 'Градска легенда'),
        ('Daily', 'Ежедневие'),
    ]

    title = models.CharField(max_length=100, help_text="")
    content = models.TextField(help_text="")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Absurd')
    created_at = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='stories'
    )

    def __str__(self):
        return f"{self.title} by {self.author.username}"