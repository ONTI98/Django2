from django.db import models


# Create your models here.

class Post(models.Model):
    text=models.CharField(max_length=240,blank=False,null=False)
    date=models.DateTimeField(auto_now=True,blank=False)

    def __str__(self):
        return (self.text)
