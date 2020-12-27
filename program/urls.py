from django.urls import path
from django.conf.urls import url
from program.views import *

urlpatterns = [
    path('program', ProgramView.as_view(), name='program'),
    path('program/activity', ActivityView.as_view(), name='activities'),
    path('', PillarView.as_view(), name='pillar'),
    path('venue', VenueView.as_view(), name='venue'),
    path('venue/addVenue', VenueRegisterView.as_view(), name='register_venue'),
    path('venue/addVenue/location', LocationView.as_view(), name='pillar')
    
]