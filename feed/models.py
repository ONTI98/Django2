from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):
    text=models.CharField(max_length=240,blank=False,null=False)
    date=models.DateTimeField(auto_now=True,blank=False)
    author=models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    def __str__(self):
        return (self.text)
