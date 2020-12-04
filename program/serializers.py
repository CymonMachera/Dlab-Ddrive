from rest_framework import serializers

from account.models import Pillar

class ProgramSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Pillar
        fields = ["name"]
    
