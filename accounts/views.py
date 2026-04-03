from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView, CreateView
from django.urls import reverse_lazy
from .models import Storyteller
from .forms import StorytellerChangeForm, StorytellerCreationForm


class RegisterView(CreateView):
    form_class = StorytellerCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Storyteller
    form_class = StorytellerChangeForm
    template_name = 'accounts/profile_edit.html'
    success_url = reverse_lazy('story-list')

    def get_object(self, queryset=None):
        return self.request.user