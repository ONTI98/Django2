from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import DetailView

# Create your views here.

class ProfileDetailView(DetailView):

    model=User
    http_method_names=["get"]
    template_name="profile_details.html"
    context_object_name="user"
    slug_field="username"
    slug_url_kwarg="username"




