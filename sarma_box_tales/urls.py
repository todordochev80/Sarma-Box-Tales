from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from common.views import HomeView
from stories.api_views import StoryListAPIView, StoryDetailAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('accounts/', include('accounts.urls')),
    path('stories/', include('stories.urls')),
    path('', include('common.urls')),
    path('comments/', include('actions.urls')),
    path('api/stories/', StoryListAPIView.as_view(), name='api-stories-list'),
    path('api/stories/<int:pk>/', StoryDetailAPIView.as_view(), name='api-story-detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
