from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework.permissions import IsAuthenticated,  AllowAny
from rest_framework import status
from safedelete.models import HARD_DELETE
from django.http import Http404
from users.serializer import UserSerializer
from rest_framework.response import Response
from shared.serializer import *
from shared.models import *

# Create your views here.
'''          Shared Files  Zone             '''
#VIew to upload share a document
class AddSharedFileView(APIView):
    parser_class = (FileUploadParser,)
    serializer_class = SharedFileSerializer
    permission_classes = [ AllowAny]
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_201_CREATED
            serializer.save()
            
            return Response(serializer.data, status=status_code)

#Retrieve, update or delete a shared file instance. 
class SharedFileUpdateView(APIView):
    parser_class = (FileUploadParser,)
    serializer_class = SharedFileSerializer
    permission_classes = [ AllowAny]
    def get_object(self, pk):
        try:
            return SharedFile.objects.all().filter( shared_by_id = pk)
        except SharedFile.DoesNotExist:
            raise Http404

    def put(self, request, *args, **kwargs):
        shared_file_key = self.get_object(self.kwargs.get('file_id', ''))
        serializer = self.serializer_class(shared_file_key, data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_201_CREATED
            serializer.save()
            return Response(serializer.data, status=status_code)

    def get(self, request, *args, **kwargs):
        shared_file = self.get_object(self.kwargs.get('file_id', ''))
        serializer = SharedFileSerializer(shared_file)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        shared_file = self.get_object(self.kwargs.get('file_id', ''))
        shared_file.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

'''          Shared Folder  Zone             '''
#VIew to upload share a document
class AddSharedFolderView(APIView):
    serializer_class = SharedFileSerializer
    permission_classes = [ AllowAny]
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_201_CREATED
            serializer.save()
            
            return Response(serializer.data, status=status_code)

#Retrieve, update or delete a shared file instance. 
class SharedFolderUpdateView(APIView):
    serializer_class = SharedFolderSerializer
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return SharedFolder.objects.all().filter( shared_by_id = pk)
        except SharedFolder.DoesNotExist:
            raise Http404

    def put(self, request, *args, **kwargs):
        shared_folder_key = self.get_object(self.kwargs.get('folder_id', ''))
        serializer = self.serializer_class(shared_folder_key, data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_201_CREATED
            serializer.save()
            return Response(serializer.data, status=status_code)

    def get(self, request, *args, **kwargs):
        shared_folder = self.get_object(self.kwargs.get('folder_id', ''))
        serializer = SharedFolderSerializer(shared_folder)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        shared_folder = self.get_object(self.kwargs.get('folder_id', ''))
        shared_folder.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

'''                Shared Zone  (the shared button)                '''
class UserSharedFolderFileView(APIView):
    serializer_class = UserSerializer
    permission_classes = [ AllowAny]

    def get_object(self, pk):    #get shared folder
        try:
            return SharedFolder.objects.all().filter( shared_to = pk)
        except SharedFolder.DoesNotExist:
            raise Http404
    def get_objects(self, pk):   #get shared files 
        try:
            return SharedFile.objects.all().filter( shared_to = pk)
        except Uploads.DoesNotExist:
            raise Http404
   
    def get(self, request,*args, **kwargs):
        serializer = {}
        folder = self.get_object(self.kwargs.get('pk', ''))
        filee = self.get_objects(self.kwargs.get('pk', ''))
        serializer['folders'] = SharedFolderSerializer(folder, many=True).data
        serializer['files'] = SharedFileSerializer(filee, many=True).data
        return Response(serializer)