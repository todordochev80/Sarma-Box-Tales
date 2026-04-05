from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts.models import Storyteller
from .forms import StoryCreateForm
from django.db.models import Q
from .models import Story, Category, Tag
from stories.models import Story
from actions.forms import CommentForm



class StoryListView(ListView):
    model = Story
    template_name = 'stories/story_list.html'
    context_object_name = 'stories'
    paginate_by = 6
    ordering = ['-created_at']

    def get_queryset(self):
        queryset = super().get_queryset()

        query = self.request.GET.get('q')
        category_id = self.request.GET.get('category')
        author_id = self.request.GET.get('author')
        tag_id = self.request.GET.get('tag')

        if query:
            queryset = queryset.filter(Q(title__icontains=query) | Q(content__icontains=query))
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        if author_id:
            queryset = queryset.filter(author_id=author_id)
        if tag_id:
            queryset = queryset.filter(tags__id=tag_id)

        return queryset.order_by('-created_at').distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['authors'] = Storyteller.objects.filter(stories__isnull=False).distinct()
        context['all_tags'] = Tag.objects.all()
        return context





class StoryDetailView(DetailView):
    model = Story
    template_name = 'stories/story_detail.html'
    context_object_name = 'story'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context



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