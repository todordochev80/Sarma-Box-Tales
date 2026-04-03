from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Storyteller

class StorytellerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Storyteller
        fields = ("username", "email", "nickname")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})



class StorytellerChangeForm(UserChangeForm):
    password = None
    class Meta:
        model = Storyteller
        fields = ("nickname", "bio", "location", "website")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})