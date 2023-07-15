import unittest
from django.test import TestCase
from django.urls import reverse
from .models import TodoTask
from .views import index, create_task


class PagesTestCase(TestCase):
    def setUp(self):
        self.task = TodoTask.objects.create(text='Test task')

    def test_index(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.task.text)

    def test_create_task(self):
        response = self.client.post(reverse('create_task'), {'task_text': 'New task'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index')) 
        self.assertEqual(TodoTask.objects.count(), 2)


