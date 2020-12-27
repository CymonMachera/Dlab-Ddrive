from rest_framework import serializers

from dlab.models import *

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = "__all__"

#serializer to upload files in the database
class OrganizationSerializer(serializers.ModelSerializer):
     class Meta:
        model = Organization
        fields = "__all__"

class ProfileSerializer(serializers.ModelSerializer):
     class Meta:
        model = Profile
        fields = "__all__"