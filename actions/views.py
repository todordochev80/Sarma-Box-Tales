from django.views.generic import CreateView
from django.shortcuts import get_object_or_404
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