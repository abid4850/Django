from django.test import TestCase
from django.urls import reverse
from .models import Post


class App2ViewsTest(TestCase):
    def setUp(self):
        Post.objects.create(title='Test post', body='Body')

    def test_index_status_code(self):
        resp = self.client.get(reverse('app2:index'))
        self.assertEqual(resp.status_code, 200)

    def test_index_contains_post(self):
        resp = self.client.get(reverse('app2:index'))
        self.assertContains(resp, 'Test post')
