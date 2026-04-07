from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import UserLoginForm

from .views import RegisterView, ProfileUpdateView, ProfileDetailView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'),
    path('profile/edit/', ProfileUpdateView.as_view(), name='profile-edit'),
    path('login/', auth_views.LoginView.as_view(
        template_name='accounts/login.html',
        authentication_form=UserLoginForm
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]