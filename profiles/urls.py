from django.urls import path

from  .views import *

app_name="profile"

urlpatterns=[
    path("profile/<str:username>",ProfileDetailView.as_view(),name="profile_details")
]