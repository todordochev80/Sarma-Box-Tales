from django.urls import path
from .views import RegisterView, ProfileUpdateView
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    # ТОВА Е ВАЖНАТА ЛИНИЯ:
    path('profile/edit/', ProfileUpdateView.as_view(), name='profile-edit'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]