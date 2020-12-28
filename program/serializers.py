from rest_framework import serializers

from account.models import Pillar
from program.models import *

class PillarSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Pillar  
        fields = "__all__"
        
        
class ProgramSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = Program  
        fields = "__all__"
        


class ActivitySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = Activity
        fields = "__all__"


'''              venues zone           '''
class VenueSerializer(serializers.ModelSerializer):
     class Meta:
        model = Venue
        fields = "__all__"

class VenueDetailSerializer(serializers.ModelSerializer):
     class Meta:
        model = Venue_detail
        fields = "__all__"

class LocationSerializer(serializers.ModelSerializer):
     class Meta:
        model = Location
        fields = "__all__"
