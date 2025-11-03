from django import forms
from django.contrib.auth.models import  User
from .models import Profile
from django.views.generic import DetailView
from allauth.account.forms import LoginForm

from allauth.account.fields import EmailField, PasswordField




#update first_name,last_name and email. This is linked to the User model
class UpdateUserDetails(forms.ModelForm):

     first_name=forms.CharField( max_length=240,
                                required=True,
                                widget=forms.TextInput(attrs={'class':'form-control'}))
     last_name=forms.CharField( max_length=240,
                                required=True,
                                widget=forms.TextInput(attrs={'class':'form-control'}))
     email=forms.EmailField( max_length=240,
                                required=True,
                                widget=forms.TextInput(attrs={'class':'form-control'}))
     
     class Meta:
          model=User
          fields=['first_name','last_name','email']
     
     
#update profile photo
class UpdateProfilePhoto(forms.ModelForm):

     image=forms.ImageField(label="Profile photo",widget=forms.FileInput(attrs={'class':'form-control'}))

     class Meta:
          model=Profile
          fields=['image']


