from django.views.generic import TemplateView
from stories.models import Story

class HomeView(TemplateView):
    template_name = 'common/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = Story.objects.all().order_by('-created_at')[:3]
        return context