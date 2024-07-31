from django.urls import path, include
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from program.views import *

urlpatterns = [
    path('', PillarView.as_view(), name='pillar'),
    path('<int:pk>/', PillarUpdateView.as_view(), name='pillar_update'),

    path('<int:pk>/programs/', PillarProgramView.as_view(), name='pillar_program'),
    path('<int:pk>/programs/addprogram/', ProgramView.as_view(), name='add_program'),
    path('<int:pk>/programs/<int:pk_alt>/', ProgramUpdateView.as_view(), name='program_update'),

    path('<int:pk>/programs/<int:pk_alt>/activities/', ProgramActivityView.as_view(), name='Program_activities'),
    path('<int:pk>/programs/<int:pk_alt>/activities/addactivity/', ActivityView.as_view(), name='add_activities'),
    path('<int:pk>/programs/<int:pk_alt>/activities/<int:activity_id>/', ActivityUpdateView.as_view(), name='activities_update'),

    path('<int:pk>/programs/<int:pk_alt>/activities/<int:activity_id>/coordinator/', ActivityCoordinatorView.as_view(), name='activities_coordinator'),
    path('<int:pk>/programs/<int:pk_alt>/activities/<int:activity_id>/coordinator/addcoordinator/', CoordinatorView.as_view(), name='add_coordinator'),
    path('<int:pk>/programs/<int:pk_alt>/activities/<int:activity_id>/coordinator/<int:coordinator_id>/', CoordinatorUpdateView.as_view(), name='add_coordinator'),

    path('<int:pk>/programs/<int:pk_alt>/activities/<int:activity_id>/collaborator/', ActivityCollaboratorsView.as_view(), name='activities_collaborator'),
    path('<int:pk>/programs/<int:pk_alt>/activities/<int:activity_id>/collaborator/addcollaborator/', CollaboratorsView.as_view(), name='add_collaborator'),
    path('<int:pk>/programs/<int:pk_alt>/activities/<int:activity_id>/collaborator/<int:collaborator_id>/', CollaboratorsUpdateView.as_view(), name='add_collaborator'),

    path('<int:pk>/programs/<int:pk_alt>/activities/<int:activity_id>/facilitator/', ActivityFacilitatorView.as_view(), name='activities_collaborator'),
    path('<int:pk>/programs/<int:pk_alt>/activities/<int:activity_id>/facilitator/addfacilitator/', FacilitatorView.as_view(), name='add_collaborator'),
    path('<int:pk>/programs/<int:pk_alt>/activities/<int:activity_id>/facilitator/<int:facilitator_id>/', FacilitatorUpdateView.as_view(), name='add_collaborator'),

    #Venues urls
    path('venue/', VenueView.as_view(), name='venues'),
    path('venue/addvenue/', AddVenueView.as_view(), name='add_venue'),
    path('venue/<int:pk>/', VenueUpdateView.as_view(), name='register_venue_update'),

    path('<int:pk>/programs/<int:pk_alt>/activities/<int:activity_id>/venueusage/', ActivityVenueUsageView.as_view(), name='venue_usage'),
    path('<int:pk>/programs/<int:pk_alt>/activities/<int:activity_id>/venueusage/addvenueusage/', AddVenueUsageView.as_view(), name='add_venue_usage'),
    path('<int:pk>/programs/<int:pk_alt>/activities/<int:activity_id>/venueusage/<int:venueusage_id>/', VenueUsageUpdateView.as_view(), name='venue_usage_update'),

    
    path('venue/location', LocationView.as_view(), name='location'),
    path('venue/location/<int:pk>/', LocationUpdateView.as_view(), name='location_update'),

    #include url from documentations  
    path('<int:pk>/programs/<int:pk_alt>/activities/<int:activity_id>/files/', include('documentation.urls')),
        
]

urlpatterns = format_suffix_patterns(urlpatterns, suffix_required=False, allowed=['json', 'html'])