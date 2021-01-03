from rest_framework import serializers

from documentation.models import *

class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = "__all__"


#serializer to upload files in the database
class FileSerializer(serializers.ModelSerializer):
     class Meta:
        model = Uploads
        fields = "__all__"