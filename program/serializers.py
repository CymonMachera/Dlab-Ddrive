from rest_framework import serializers

from account.models import Pillar
from program.models import Program, Activity

class PillarSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Pillar  
        fields = ["name", 'pillar_desc']
        read_only_fields = ['name','pillar_desc']
class PillarProgramSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Pillar  
        fields = ["name", 'pillar_desc']
        read_only_fields = ['pillar_desc']
        
class ProgramSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = Program  
        fields = ['id',"name", 'program_desc']
        read_only_fields = ['name','program_desc']
        


class ActivitySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Activity
        fields = ['id',"name",'type_of_activity', 'Participants_number','Start_time','End_time','program_desc']
        read_only_fields = ["name",'type_of_activity', 'Participants_number','Start_time', 'End_time', 'program_desc']
