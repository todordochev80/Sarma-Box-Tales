from django import forms
from .models import Story


class StoryCreateForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ['title', 'content', 'category', 'tags']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Заглавие на историята'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-select'}),
        }