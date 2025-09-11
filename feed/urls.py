from django.urls import path
from .views import *
#from . import views

app_name="feed"

urlpatterns=[path('',HomePage.as_view(),name="index"),
              ]
