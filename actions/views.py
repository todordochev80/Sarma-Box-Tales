from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from .models import Comment
from .forms import CommentForm
from stories.models import Story


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.story = get_object_or_404(Story, pk=self.kwargs['story_id'])


        initial_comment_id = self.request.POST.get('initial_comment_id')
        if initial_comment_id:
            form.instance.initial_comment = get_object_or_404(Comment, id=initial_comment_id)

        return super().form_valid(form)

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER', '/')



class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'actions/comment_edit.html'

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        return self.object.story.get_absolute_url() if hasattr(self.object.story, 'get_absolute_url') else reverse_lazy('story-detail', kwargs={'pk': self.object.story.id})

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'actions/comment_confirm_delete.html'

    def test_func(self):
        comment = self.get_object()
        is_moderator = self.request.user.groups.filter(name='Moderators').exists()
        return self.request.user == comment.author or is_moderator

    def get_success_url(self):
        return reverse_lazy('story-detail', kwargs={'pk': self.object.story.id})