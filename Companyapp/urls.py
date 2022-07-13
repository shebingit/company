from django.conf import settings
from .import views
from django.views import *
from django.urls import  path
from django.conf.urls.static import static

urlpatterns =[  path('',views.index,name='index'),
path('load',views.load,name='load'),

  ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)