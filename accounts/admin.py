from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import StorytellerCreationForm, StorytellerChangeForm
from .models import Storyteller


@admin.register(Storyteller)
class StorytellerAdmin(UserAdmin):
    add_form = StorytellerCreationForm
    form = StorytellerChangeForm
    model = Storyteller
    list_display = ["username", "email", "nickname", "rank", "is_staff", 'avatar']

    fieldsets = UserAdmin.fieldsets + (
        ("Допълнителна информация", {"fields": ("nickname", "bio", "rank", 'avatar')}),
    )