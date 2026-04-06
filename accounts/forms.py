from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Storyteller
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class StorytellerCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label="Имейл адрес",
        error_messages={
            'required': 'Това поле е задължително',
            'invalid': 'Несъществува такъв е-мейл, пробвай отново!',
            'unique': 'Този имейл вече е регистриран при нас.'
        }
    )
    class Meta(UserCreationForm.Meta):
        model = Storyteller
        fields = ("username", "email", "nickname")
        error_messages = {
            'username': {
                'unique': 'Потребител с това име вече съществува. Избери си друго име.',
                'required': 'Потребителското име е задължително.',
            },
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if Storyteller.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError(
                "Вече има регистриран потребител с това име!"
            )
        return username


    def clean_password2(self):
        p1 = self.cleaned_data.get("password1")
        p2 = self.cleaned_data.get("password2")
        if p1 and p2 and p1 != p2:
            raise forms.ValidationError(
                "Паролите не съвпадат! Напиши ги внимателно."
            )
        return p2


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})



class StorytellerChangeForm(UserChangeForm):
    password = None
    class Meta:
        model = Storyteller
        fields = ("username", "email", "nickname", "bio", "location", "website", "avatar")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if 'username' in self.fields:
            self.fields['username'].disabled = True
            self.fields['username'].label = "Потребителско име (не се променя)"

        if 'email' in self.fields:
            self.fields['email'].disabled = True
            self.fields['email'].label = "Имейл (не се променя)"

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

    error_messages = {
        'invalid_login': (
            "Потребителското име или паролата не съвпадат. "
            "Провери дали не си натиснал Caps Lock по погрешка."
        ),
    }

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user_cache = User.objects.filter(username__iexact=username).first()

            if user_cache:
                self.user_cache = authenticate(
                    self.request,
                    username=user_cache.username,
                    password=password
                )
            else:
                self.user_cache = None

            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data