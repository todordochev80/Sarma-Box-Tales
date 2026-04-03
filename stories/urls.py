from django.urls import path
from .views import StoryListView, StoryDetailView, StoryCreateView, StoryUpdateView, StoryDeleteView

urlpatterns = [
    path('', StoryListView.as_view(), name='story-list'),
    path('<int:pk>/', StoryDetailView.as_view(), name='story-detail'),
    path('create/', StoryCreateView.as_view(), name='story-create'),
    path('<int:pk>/edit/', StoryUpdateView.as_view(), name='story-edit'),
    path('<int:pk>/delete/', StoryDeleteView.as_view(), name='story-delete'),

]