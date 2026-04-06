from django.test import TestCase
from django.urls import reverse
from accounts.models import Storyteller
from .models import Story, Category
from stories.forms import StoryCreateForm

class StoriesTests(TestCase):
    def setUp(self):
        self.user = Storyteller.objects.create_user(username='toshko', password='12admin34')
        self.category = Category.objects.create(name='Смешни')
        self.story = Story.objects.create(
            title='Тестов разказ',
            content='Съдържание....',
            author=self.user,
            category=self.category
        )

    def test_story_content(self):
        self.assertEqual(self.story.title, 'Тестов разказ')
        self.assertEqual(str(self.story), 'Тестов разказ by toshko')

    def test_story_list_view(self):
        response = self.client.get(reverse('story-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Тестов разказ')

    def test_story_detail_view(self):
        response = self.client.get(reverse('story-detail', kwargs={'pk': self.story.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Съдържание....')

    def test_create_story_requires_login(self):
        response = self.client.get(reverse('story-create'))
        self.assertEqual(response.status_code, 302)

    def test_api_list_status(self):
        response = self.client.get(reverse('api-stories-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')


    def test_search_works(self):
        response = self.client.get(reverse('story-list') + '?q=Тестов')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Тестов разказ')

    def test_filter_by_category(self):
        response = self.client.get(reverse('story-list') + f'?category={self.category.id}')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Смешни')

    def test_api_detail_view(self):
        url = reverse('api-story-detail', kwargs={'pk': self.story.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'Тестов разказ')


    def test_story_form_invalid_data(self):
        form = StoryCreateForm(data={'title': '', 'content': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)

    def test_profile_page_requires_login(self):
        response = self.client.get(reverse('profile-detail', kwargs={'pk': self.user.pk}))
        self.assertEqual(response.status_code, 302)