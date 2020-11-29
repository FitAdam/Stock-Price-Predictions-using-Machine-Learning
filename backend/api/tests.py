from django.test import TestCase

from .models import Post
from django.contrib.auth.models import User


class PostModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.get(username='admin')
        #admin.user = user
        Post.objects.create(author=user, title='Tesla Y', body='The great family car.')
    
    def test_title_content(self):
        post = Post.objects.get(id=2)
        expected_object_name = f'{post.title}'
        self.assertEquals(expected_object_name, 'Tesla Y')
    
    def test_body_content(self):
        post = Post.objects.get(id=2)
        expected_object_name = f'{post.body}'
        self.assertEquals(expected_object_name, 'The great family car.')