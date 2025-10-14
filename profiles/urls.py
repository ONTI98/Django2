from django.urls import path
from  .views import *


app_name="profile"

urlpatterns=[
    path("profile/<str:username>",ProfileDetailView.as_view(),name="profile_details"),
    path("profile/<str>:username/follow/",FollowView.as_view(),name="follow" ),
    path("profile/",ProfileView.as_view(),name="profile"),
    
    ]