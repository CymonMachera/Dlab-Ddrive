from django.urls import path
from django.conf.urls import url
from .views import *

urlpatterns = [
    path('program', ProgramView.as_view(), name='programs'),
    path('program/activity', ActivityView.as_view(), name='activities'),
    path('', PillarView.as_view(), name='pillar')
    
]