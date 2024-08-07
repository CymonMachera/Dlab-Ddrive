from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from safedelete.models import HARD_DELETE
from django.http import Http404
from users.serializer import UserSerializer
from account.models import CustomUser
from documentation.models import *
from documentation.serializers import *
from rest_framework.response import Response

# Create your views here.

'''                Trash Zone                  '''
class UserFolderFileTrashView(APIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):    #get deleted folder
        try:
            return Folder.objects.deleted_only().filter( creator_id = pk)
        except Folder.DoesNotExist:
            raise Http404
    def get_objects(self, pk):   #get deleted files belonging to a folder
        try:
            return Uploads.objects.deleted_only().filter( folder__id__isnull = False , uploader_name_id = pk)
        except Uploads.DoesNotExist:
            raise Http404
    def get_objectss(self, pk):  # get deleted files in the base activity
        try:
            return Uploads.objects.deleted_only().filter( program__id__isnull = False , uploader_name_id = pk)
        except Uploads.DoesNotExist:
            raise Http404

   
    def get(self, request,*args, **kwargs):
        serializer = {}
        folder = self.get_object(self.kwargs.get('pk', ''))
        filee = self.get_objects(self.kwargs.get('pk', ''))
        filee2 = self.get_objectss(self.kwargs.get('pk', ''))
        serializer['folders'] = FolderSerializer(folder, many=True).data
        serializer['files_level1'] = FileSerializer(filee2, many=True).data
        serializer['files_level2'] = FileSerializer(filee, many=True).data
        return Response(serializer)

'''              Undelete / Delete File and folders from Trash        '''

#Trash Files update view
class TrashFilesUpdateView(APIView):
    parser_class = (FileUploadParser,)
    serializer_class = FileSerializer
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Uploads.objects.get(pk=pk)
        except Uploads.DoesNotExist:
            raise Http404
    
    def get(self, request, *args, **kwargs):
        filee = self.get_object(self.kwargs.get('file_id', ''))
        serializer = FileSerializer(filee)
        return Response(serializer.data)
    
    def put(self, request, *args, **kwargs):
        filee = self.get_object(self.kwargs.get('file_id', ''))
        filee.undelete()
        serializer = self.serializer_class(filee, data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_201_CREATED
            serializer.save()
            return Response(serializer.data, status=status_code)

    def delete(self, request, *args, **kwargs):
        filee = self.get_object(self.kwargs.get('file_id', ''))
        filee.delete(force_policy= HARD_DELETE, **kwargs)
        return Response(status=status.HTTP_204_NO_CONTENT)

#Trash Folders update view
class TrashFoldersUpdateView(APIView):
    serializer_class = FolderSerializer
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Folder.objects.get(pk=pk)
        except Folder.DoesNotExist:
            raise Http404
    def get(self, request, *args, **kwargs):
        folder = self.get_object(self.kwargs.get('folder_id', ''))
        serializer = FolderSerializer(folder)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        folder = self.get_object(self.kwargs.get('folder_id', ''))
        folder.undelete()
        serializer = self.serializer_class(folder, data=request.data)
        valid = serializer.is_valid(raise_exception=True)
        if valid:
            status_code = status.HTTP_201_CREATED
            serializer.save()
            return Response(serializer.data, status=status_code)
        

    def delete(self, request, *args, **kwargs):
        folder = self.get_object(self.kwargs.get('folder_id', ''))
        folder.delete(force_policy= HARD_DELETE, **kwargs)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    