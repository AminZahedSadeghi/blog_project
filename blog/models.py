from django.db import models
from django.shortcuts import reverse


class Post(models.Model):
    STATUS_CHOICES = (
        ('pub', 'Published'),
        ('drf', 'Draft'),
    )
    title = models.CharField(max_length=100)
    text = models.TextField()
    post_time_create = models.DateTimeField(auto_now_add=True)
    post_time_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(to='auth.User', on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS_CHOICES, max_length=3)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_list')
