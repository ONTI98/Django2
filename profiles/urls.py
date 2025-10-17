from django.urls import path
from  .views import *


app_name="profile"

urlpatterns=[
    path("profile/<str:username>",ProfileDetailView.as_view(),name="profile_details"),
    path("profile/<str>:username/follow/",FollowView.as_view(),name="follow" ),
    path("profile/",ProfileView.as_view(),name="profile"),
    path("change_password/",ChangePasswordView.as_view(),name="password"),
    path("update_user/",update_profile_information,name="update_user_details"),
    path("update_avatar/",update_profile_information,name="update_avatar")
    ]