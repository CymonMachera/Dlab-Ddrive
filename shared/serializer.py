from rest_framework import serializers
from shared.models import *

class SharedFolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SharedFolder
        fields = "__all__"


class SharedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SharedFile
        fields = "__all__"

