from django.test import TestCase
from .models import Storyteller
from .forms import StorytellerCreationForm


class accountsTest(TestCase):

    def test_create_user(self):
        user = Storyteller.objects.create_user(
            username='toshko',
            password='12admin34',
            email='toshko@abv.bg'
        )
        self.assertEqual(user.username, 'toshko')
        self.assertTrue(user.is_active)

    def test_create_superuser(self):
        admin = Storyteller.objects.create_superuser(
            username='admin',
            password='12admin34',
            email='admin@abv.bg'
        )
        self.assertTrue(admin.is_staff)
        self.assertTrue(admin.is_superuser)

    def test_register_form_valid(self):
        form_data = {
            'username': 'user1',
            'email': 'user1@abv.bg',
            'password1': '12admin34',
            'password2': '12admin34',
        }
        form = StorytellerCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_register_form_invalid_passwords(self):
        form_data = {
            'username': 'user1',
            'email': 'user1@abv.bg',
            'password1': 'pass123',
            'password2': 'admin',
        }
        form = StorytellerCreationForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_register_form_no_email(self):
        form_data = {
            'username': 'user1',
            'password1': '12admin34',
            'password2': '12admin34',
        }
        form = StorytellerCreationForm(data=form_data)
        self.assertFalse(form.is_valid())