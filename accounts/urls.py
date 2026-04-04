from django.urls import path
from .views import RegisterView, ProfileUpdateView
from django.contrib.auth import views as auth_views
from .forms import UserLoginForm

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),

    path('profile/edit/', ProfileUpdateView.as_view(), name='profile-edit'),
    path('login/', auth_views.LoginView.as_view(
        template_name='accounts/login.html',
        authentication_form=UserLoginForm
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]