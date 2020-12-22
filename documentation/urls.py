from django.urls import path
from django.conf.urls import url
from .views import *

urlpatterns = [
    path('', UploadsView.as_view(), name='uploads')
]