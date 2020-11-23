from django.contrib import admin
from django.urls import path, include
from . import views
from home.views import DlabHome

urlpatterns = [
    
    path('', DlabHome.as_view(), name = 'home'),
    
]
