
from django.urls import path
from .views import CommentCreateView, CommentUpdateView, CommentDeleteView

urlpatterns = [

    path('create/<int:story_id>/', CommentCreateView.as_view(), name='comment-create'),
    path('<int:pk>/edit/', CommentUpdateView.as_view(), name='comment-edit'),
    path('<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]
