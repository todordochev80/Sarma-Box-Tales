from django.contrib.auth.models import AbstractUser
from django.db import models

class Storyteller(AbstractUser):
    nickname = models.CharField(
        max_length=50,
        blank=True,
        # TODO - промени името
        help_text=""
    )
    bio = models.TextField(
        max_length=500,
        blank=True,
        # TODO - промени инфото
        help_text=""
    )
    rank = models.CharField(
        max_length=30,
        # TODO - промени ранглиста
        default="Fresh Sarma"
    )

    def __str__(self):
        return self.username
