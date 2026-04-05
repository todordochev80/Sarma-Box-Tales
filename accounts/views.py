from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView, CreateView
from django.urls import reverse_lazy
from .models import Storyteller
from .forms import StorytellerChangeForm, StorytellerCreationForm
from .tasks import send_welcome_email

class RegisterView(CreateView):
    form_class = StorytellerCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)

        user_email = form.cleaned_data.get('email')
        username = form.cleaned_data.get('username')

        send_welcome_email.delay(user_email, username)

        return response

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Storyteller
    form_class = StorytellerChangeForm
    template_name = 'accounts/profile_edit.html'
    success_url = reverse_lazy('story-list')

    def get_object(self, queryset=None):
        return self.request.user