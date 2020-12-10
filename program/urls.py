from django.urls import path
from django.conf.urls import url
from .views import *

urlpatterns = [
    path('', ProgramView.as_view(), name='programs'),
    path('activities', ActivityView.as_view(), name='activities'),
    
]