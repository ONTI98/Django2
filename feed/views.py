from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
from django.views.generic import *
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin #will force user to be authenticated
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

class CreateNewPostView(LoginRequiredMixin,CreateView):
    model=Post
    template_name="feed/create.html"
    fields=["text"]
    success_url="/"

    def dispatch(self,request,*args,**kwargs):
        self.request=request
        return super().dispatch(request,*args,**kwargs)
        
    def form_valid(self,form):
        obj=form.save(commit=False)
        obj.author=self.request.user
        obj.save()
        return super().form_valid(form)
    


