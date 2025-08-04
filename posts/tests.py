from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from .models import Post

User = get_user_model()


class PostTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.post = Post.objects.create(author=self.user, text="Test post")

    def test_post_creation(self):
        self.client.force_authenticate(user=self.user)
        url = reverse("post-list")
        data = {"text": "New post"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
