
from django.urls import path
from .views import CommentCreateView

urlpatterns = [

    path('create/<int:story_id>/', CommentCreateView.as_view(), name='comment-create'),
]