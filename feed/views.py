from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
from django.views.generic import *
# Create your views here.



class HomePage(ListView):
    model=Post
    template_name="feed/homepage.html"
    context_object_name="posts"
    http_method_names=["get"]
    queryset=Post.objects.all().order_by("-id")[0:30] #arranges posts by descending order

class PostDetailView(DetailView):
    http_method_names=["get"]
    template_name="feed/detail.html"
    model=Post
    context_object_name="post"
