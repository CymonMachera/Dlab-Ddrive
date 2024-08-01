from django.urls import path
from django.conf.urls import url
from .views import *

urlpatterns = [
    path('', AdverisementView.as_view(), name='advertisement'),
   
]