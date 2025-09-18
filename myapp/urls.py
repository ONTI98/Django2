
from django.contrib import admin
from django.urls import include,path
from feed import urls as feed_urls
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(feed_urls,namespace="feed")),
    path('',include("allauth.urls")),

    ] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns+=[
        path('__reload__/',include("django_browser_reload.urls"))
    ]
