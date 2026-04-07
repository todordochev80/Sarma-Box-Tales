from django.contrib.auth.models import AbstractUser
from django.db import models

class Storyteller(AbstractUser):
    nickname = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name="Псевдоним",
        help_text="Името, с което ще се подписвате под историите."
    )
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    email = models.EmailField(unique=True, blank=False)

    bio = models.TextField(
        max_length=500,
        blank=True,
        verbose_name="Биография",
        help_text="Разкажете накратко за Вашия творчески опит."
    )
    location = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Регион/Град",
        help_text="От коя част на света е историята Ви?"
    )
    rank = models.CharField(
        max_length=30,
        default="Лозова сърмичка",
        verbose_name="Ранг",
        help_text="Вашият статус в общността на 'Разкази от кутията със сармички'"
    )
    website = models.URLField(
        blank=True,
        verbose_name="Личен сайт/Блог"
    )

    class Meta:
        verbose_name = "Разказвач"
        verbose_name_plural = "Разказвачи"

    def __str__(self):
        return self.nickname if self.nickname else self.username

