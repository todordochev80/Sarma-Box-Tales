from django import forms
from .models import Story


class StoryCreateForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ['title', 'content', 'category', 'tags']

        labels = {
            'title': 'Заглавие на твоята история 📖',
            'category': 'Избери кутия (Категория) 🗳️',
            'content': 'Разкажи ни всичко... ✍️',
            'tags': 'Етикети (Тагове) 🏷️',
        }

        help_texts = {
            'title': 'Заглавието трябва да е грабващо и абсурдно.',
            'content': 'Минимално 50 символа за истинска история.',
        }

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Напр.: Приключенията на една сърма...'}),
            'content': forms.Textarea(attrs={'placeholder': 'Имало едно време в една тенджера...', 'rows': 5}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        for field_name, field in self.fields.items():
            widget_type = field.widget.__class__.__name__
            if widget_type in ['Select', 'SelectMultiple']:
                field.widget.attrs.update({'class': 'form-select'})
            else:
                field.widget.attrs.update({'class': 'form-control'})

        self.fields['title'].error_messages.update({
            'required': 'Е, не може без заглавие! Как ще го кръстиш?',
            'max_length': 'Твърде дълго заглавие, дай малко по-късинко а?'
        })