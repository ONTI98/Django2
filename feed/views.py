from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
from django.views.generic import *
# Create your views here.



class HomePage(ListView):
    model=Post
    template_name="homepage.html"
    context_object_name="posts"
    http_method_names=["get"]
    queryset=Post.objects.all().order_by("-id") #arranges posts by descending order

