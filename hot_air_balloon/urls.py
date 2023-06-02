from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from hot_air_balloon.views import index
from hot_air_balloon.views import home
from kolokviumska1 import settings

urlpatterns = [
                  path('list', index, name='index'),
                  path('', home, name='home'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
