from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import StoryCreateForm

from stories.models import Story



class StoryListView(ListView):
    model = Story
    template_name = 'stories/story_list.html'
    context_object_name = 'stories'
    ordering = ['-created_at']


class StoryDetailView(DetailView):
    model = Story
    template_name = 'stories/story_detail.html'
    context_object_name = 'story'



class StoryCreateView(LoginRequiredMixin, CreateView):
    model = Story
    form_class = StoryCreateForm
    template_name = 'stories/story_create.html'
    success_url = reverse_lazy('story-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class StoryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Story
    form_class = StoryCreateForm
    template_name = 'stories/story_edit.html'
    success_url = reverse_lazy('story-list')

    def test_func(self):
        story = self.get_object()
        return self.request.user == story.author

class StoryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Story
    template_name = 'stories/story_confirm_delete.html'
    success_url = reverse_lazy('story-list')

    def test_func(self):
        story = self.get_object()
        return self.request.user == story.author