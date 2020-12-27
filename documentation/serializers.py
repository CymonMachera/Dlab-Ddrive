from rest_framework import serializers

from documentation.models import *

class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = "__all__"

#serializet to get files from the database
class UploadsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = Uploads
        fields = ['id',"activity_name",'doc_name', 'uploader_name', 'doc_type','dete_uploaded','upload_path']
        read_only_fields =  ["activity_name",'doc_name', 'uploader_name', 'doc_type','dete_uploaded','upload_path']

#serializer to upload files in the database
class FileUploadSerializer(serializers.ModelSerializer):
     class Meta:
        model = Uploads
        fields = "__all__"