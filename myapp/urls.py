
from django.contrib import admin
from django.urls import path
from feed import urls as feed_urls
from django.conf.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(feed_urls,namespace="feed")),
    path('',include("allauth.urls")),
]
 