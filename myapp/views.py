from django.contrib.auth.models import User
from django.views.generic import DetailView,TemplateView
from django.contrib.auth.views import PasswordChangeView

from feed.models import Post
from followers.models import Follower

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.http import JsonResponse
from django.http import HttpResponseBadRequest

from django.urls import reverse_lazy
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate,login

# Create your views here.


class ProfileView(LoginRequiredMixin,DetailView):

     model=User
     template_name="profile.html"
     context_object_name="user"
     slug_url_kwarg="username"
     slug_field="username"


     
     def get_object(self, queryset=None):
          # If "username" is in the URL, return that user; else, return current user
          username = self.kwargs.get(self.slug_url_kwarg)
          if username:
               return get_object_or_404(User, username=username)
          return self.request.user
   
     def get_context_data(self, **kwargs):
          context=super().get_context_data(**kwargs)
          profile_photo=self.get_object().profile.image.url
          if profile_photo:
               context["profile_photo"]=profile_photo
          else:
               pass #return a default image/
          return context
         
    
 

class ProfileDetailView(DetailView):

    model=User
    http_method_names=["get"]
    template_name="profile_details.html"
    context_object_name="user"
    slug_field="username"
    slug_url_kwarg="username"


    def dispatch(self, request, *args, **kwargs):
         self.request=request
         return super().dispatch(request, *args, **kwargs)

    #get total number of posts
    def get_context_data(self,**kwargs):
    
        user=self.get_object() #set the user property
        context=super().get_context_data(**kwargs)
        context['total_posts']=Post.objects.filter(author=user).count()
        context['total_followers']=Follower.objects.filter(following=user).count()
        context['total_following']=Follower.objects.filter(followed_by=user).count()
        if self.request.user.is_authenticated:
             context["you_follow"] =Follower.objects.filter(following=user,followed_by=self.request.user).exists()
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
                       follower=Follower.objects.get(
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
                   "wording":"Unfollow" if data["action"] == "follow" else "Follow"
              }
             )
          


#update user details
@login_required
def update_profile_information(request):
     if request.method == "POST": #if the user is uploading information
          user_form=UpdateUserDetails(request.POST,instance=request.user)
          profile_form=UpdateProfilePhoto(request.POST,request.FILES,instance=request.user.profile)

          if profile_form.is_valid() and user_form.is_valid():
               user_form.save()
               profile_form.save()
               messages.success(request,("Profile updated successfully!"))

               return redirect("/")
#redireect to user profile
              
     else:
          user_form=UpdateUserDetails(instance=request.user)
          profile_form=UpdateProfilePhoto(instance=request.user)


     return render(request,"profile_update.html",{'user_form':user_form, 'profile_form':profile_form})


class ChangePasswordView(PasswordChangeView):
    template_name = 'change_password.html'
    success_url = reverse_lazy("password")

