from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import DetailView
from feed.models import Post
from followers.models import Follower
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.http import JsonResponse
from django.http import HttpResponseBadRequest
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

class FollowView(LoginRequiredMixin,View):
        http_method_names=["post"]
        
        def post(self,request,*args,**kwargs):
             
             data=request.POST.dict()
             if "action" not in data or "username" not in data:
                  return HttpResponseBadRequest("Missing data")
             try:
                   other_user=User.objects.get(username=data["username"])
             
             except  User.DoesNotExist:
                  return HttpResponseBadRequest("User not found")
             if data['action'] == "follow":
                  follower,created=Follower.objects.get_or_create(
                  followed_by=request.user,
                  following=other_user)

             else:
                    try:
                       folower=Follower.objects.get(
                            followed_by=request.user,
                            following=other_user,
                       )
                    except Follower.DoesNotExist:
                         follower=None 
                    if follower:
                         follower.delete()

             return JsonResponse(
              {
                   "success":True,
                   "wording":"unfollow" if data["action"] =="follow" else  data["action"]=="Follow"
              }
             )
          