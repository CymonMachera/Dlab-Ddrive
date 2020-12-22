from rest_framework import serializers

from documentation.models import Uploads

class UploadsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = Uploads
        fields = ['id',"activity_name",'doc_name', 'uploader_name', 'doc_type','dete_uploaded','upload_path']
        read_only_fields =  ["activity_name",'doc_name', 'uploader_name', 'doc_type','dete_uploaded','upload_path']
