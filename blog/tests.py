from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import reverse

from .models import Post


class BlogPostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='user1')
        cls.post1 = Post.objects.create(
            title='Post1 Title',
            text='Post1 Text',
            status='pub',
            author=cls.user,
        )
        cls.post2 = Post.objects.create(
            title='Post2 Title',
            text='Post2 Text',
            status='drf',
            author=cls.user,
        )

    def test_post_title_in_database(self):
        self.assertEqual(str(self.post1), 'Post1 Title')

    def test_post_list_url_by_name(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)

    def test_post_detail_by_name(self):
        response = self.client.get(reverse('post_detail', args=[self.post1.id]))
        self.assertEqual(response.status_code, 200)

    def test_post_detail_url_404_error(self):
        response = self.client.get(reverse('post_detail', args=[999]))
        self.assertEqual(response.status_code, 404)

    def test_post_draft_not_show(self):
        response = self.client.get(reverse('post_list'))
        self.assertNotContains(response, self.post2.title)

    def test_post_pub_show(self):
        response = self.client.get(reverse('post_list'))
        self.assertContains(response, self.post1.title)

    def test_show_post_title_on_post_list_view(self):
        response = self.client.get(reverse('post_list'))
        self.assertContains(response, self.post1.title)

    def test_show_post_title_on_post_detail_view(self):
        response = self.client.get(reverse('post_detail', args=[self.post1.id]))
        self.assertContains(response, self.post1.title)

    def test_post_create_view(self):
        response = self.client.post(reverse('post_create'), {
            'title': 'Some Title',
            'text': 'This is text',
            'status': 'pub',
            'author': self.user.id,
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, 'Some Title')
        self.assertEqual(Post.objects.last().text, 'This is text')

    def test_post_update_view(self):
        response = self.client.post(reverse('post_update', args=[self.post1.id]), {
            'title': 'Some Title',
            'text': 'This is text',
            'status': 'pub',
            'author': self.user.id,
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.get(pk=self.post1.id).title, 'Some Title')
        self.assertEqual(Post.objects.get(pk=self.post1.id).text, 'This is text')

    def test_post_delete_view(self):
        response = self.client.post(reverse('post_delete', args=[self.post2.id]))
        self.assertEqual(response.status_code, 302)
