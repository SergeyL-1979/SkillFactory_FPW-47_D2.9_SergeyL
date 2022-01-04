from django.http import request
from django.shortcuts import render
from django.utils.datetime_safe import datetime
from django.views.generic import ListView, DetailView

from .models import Post, Comment, Category, PostCategory


class NewsList(ListView):
    model = Post
    ordering = ['-create_date']

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['comment_post'] = Comment.objects.filter(comment_post=self.kwargs['pk'])
    #     return context


class NewsDetail(DetailView):
    model = Post
    slug_field = 'slug'


class CategoryPost(DetailView):
    model = Category
    slug_field = 'category_name'
    # category_all = Category.objects.all()





