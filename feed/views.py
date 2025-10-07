from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import TemplateView
from .models import Post
from django.views.generic import *
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin #will force user to be authenticated
# Create your views here.
from django.shortcuts import render


class HomePage(TemplateView):
    model=Post
    template_name="feed/homepage.html"
    context_object_name="posts"
    http_method_names=["get"]
    queryset=Post.objects.all().order_by("-id")[0:150] #arranges posts by descending order

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
    
    #create post method
    def post(self,request,*args,**kwargs):
       #create a new post object
       post=Post.objects.create(
           text=request.POST.get("text"),
           author=request.user,
           )
       return render(
           request,"includes/post.html",
           {
               "post":post, #from post.html
               "show_detail_link":True,
           },
           content_type="application/html"
           )

