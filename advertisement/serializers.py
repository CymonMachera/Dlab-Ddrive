from rest_framework import serializers

from .models import *

class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = "__all__"


