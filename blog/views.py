# Djagno import
from django.shortcuts import render, reverse
from django.views import generic
from django.urls import reverse_lazy

# Local import
from .models import Post
from .forms import PostForm


class PostListView(generic.ListView):
    template_name = 'blog/post_list.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return Post.objects.filter(status='pub').order_by('-post_time_modified')


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


class PostCreateView(generic.CreateView):
    form_class = PostForm
    template_name = 'blog/post_create.html'
    context_object_name = 'form'


class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_create.html'


class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    context_object_name = 'post'

    # success_url = reverse_lazy('post_list')

    def get_success_url(self):
        return reverse('post_list')
