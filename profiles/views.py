from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import DetailView
from feed.models import Post
from followers.models import Follower



# Create your views here.

class ProfileDetailView(DetailView):

    model=User
    http_method_names=["get"]
    template_name="profile_details.html"
    context_object_name="user"
    slug_field="username"
    slug_url_kwarg="username"


    #get total number of posts
    def get_context_data(self,**kwargs):
        user=self.get_object() #set the user property
        context=super().get_context_data(**kwargs)
        context['total_posts']=Post.objects.filter(author=user).count()
        context['total_followers']=Follower.objects.filter(following=user).count()
        context['total_following']=Follower.objects.filter(followed_by=user).count()

        return context
