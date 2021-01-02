from rest_framework import serializers

from account.models import Pillar
from program.models import *

class PillarSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Pillar  
        fields = "__all__"
        
        
class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program  
        fields = "__all__"
        


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = "__all__"


'''              venues zone           '''
class VenueUsageSerializer(serializers.ModelSerializer):
     class Meta:
        model = Venue
        fields = "__all__"

class VenueSerializer(serializers.ModelSerializer):
     class Meta:
        model = Venue_detail
        fields = "__all__"

class LocationSerializer(serializers.ModelSerializer):
     class Meta:
        model = Location
        fields = "__all__"

class CoordinatorSerializer(serializers.ModelSerializer):
     class Meta:
        model = Coordinator
        fields = "__all__"

class CollaboratorsSerializer(serializers.ModelSerializer):
     class Meta:
        model = Collaborators
        fields = "__all__"

class FacilitatorSerializer(serializers.ModelSerializer):
     class Meta:
        model = Facilitator
        fields = "__all__"



