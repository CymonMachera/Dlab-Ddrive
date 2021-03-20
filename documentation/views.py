from django.db.models.fields import NullBooleanField
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from django.http import Http404
from documentation.serializers import *
from program.serializers import ActivitySerializer
from rest_framework.response import Response
from documentation.models import *
# Create your views here.
'''           Folder Zone               '''
#view to create folders
class AddFolderView(APIView):
    serializer_class = FolderSerializer
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)
        if valid:
            status_code = status.HTTP_201_CREATED
            serializer.save()
            
            return Response(serializer.data, status=status_code)

#Retrieve, update or delete a folder instance. 
class FolderUpdateView(APIView):
    serializer_class = FolderSerializer
    permission_classes = [AllowAny]
    def get_object(self, pk):
        try:
            return Folder.objects.get(pk=pk)
        except Folder.DoesNotExist:
            raise Http404

    def put(self, request, *args, **kwargs):
        folder_key = self.get_object(self.kwargs.get('folder_id', ''))
        serializer = self.serializer_class(folder_key, data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_201_CREATED
            serializer.save()
            return Response(serializer.data, status=status_code)

    def get(self, request, *args, **kwargs):
        folder = self.get_object(self.kwargs.get('folder_id', ''))
        serializer = FolderSerializer(folder)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        folder = self.get_object(self.kwargs.get('folder_id', ''))
        folder.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Retrieve, update or delete a folder instance. 
class FolderLevel2UpdateView(APIView):
    serializer_class = FolderSerializer
    permission_classes = [AllowAny]
    def get_object(self, pk):
        try:
            return Folder.objects.get(pk=pk)
        except Folder.DoesNotExist:
            raise Http404

    def put(self, request, *args, **kwargs):
        folder_key = self.get_object(self.kwargs.get('folder_level2_id', ''))
        serializer = self.serializer_class(folder_key, data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_201_CREATED
            serializer.save()
            return Response(serializer.data, status=status_code)

    def get(self, request, *args, **kwargs):
        folder = self.get_object(self.kwargs.get('folder_level2_id', ''))
        serializer = FolderSerializer(folder)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        folder = self.get_object(self.kwargs.get('folder_level2_id', ''))
        folder.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

'''          File  Zone             '''
#VIew to upload  the documents
class AddFileView(APIView):
    parser_class = (FileUploadParser,)
    serializer_class = FileSerializer
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_201_CREATED
            serializer.save()
            
            return Response(serializer.data, status=status_code)

#Retrieve, update or delete a file instance. 
class FileUpdateView(APIView):
    parser_class = (FileUploadParser,)
    serializer_class = FileSerializer
    permission_classes = [AllowAny]
    def get_object(self, pk):
        try:
            return Uploads.objects.get(pk=pk)
        except Uploads.DoesNotExist:
            raise Http404

    def put(self, request, *args, **kwargs):
        file_key = self.get_object(self.kwargs.get('file_id', ''))
        serializer = self.serializer_class(file_key, data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_201_CREATED
            serializer.save()
            return Response(serializer.data, status=status_code)

    def get(self, request, *args, **kwargs):
        filee = self.get_object(self.kwargs.get('file_id', ''))
        serializer = FileSerializer(filee)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        filee = self.get_object(self.kwargs.get('file_id', ''))
        filee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

'''            ActivityFolderFile Zone           '''
class ActivityFolderFileView(APIView):
    serializer_class = ActivitySerializer
    permission_classes = [AllowAny]

    def get_object(self, pk):
        try:
            return Folder.objects.filter( activity_name_id= pk)
        except Folder.DoesNotExist:
            raise Http404
    def get_objects(self, pk):
        try:
            return Uploads.objects.filter( activity_name_id= pk)
        except Uploads.DoesNotExist:
            raise Http404

   
    def get(self, request,*args, **kwargs):
        serializer = {}
        folder = self.get_object(self.kwargs.get('activity_id', ''))
        filee = self.get_objects(self.kwargs.get('activity_id', ''))
        serializer['folders'] = FolderSerializer(folder, many=True).data
        serializer['files'] = FileSerializer(filee, many=True).data
        return Response(serializer)


'''            FolderFile Zone           '''
class FolderFileView(APIView):
    serializer_class = FolderSerializer
    permission_classes = [AllowAny]

    def get_object(self, pk):
        try:
            return Folder.objects.filter( parent_id= pk)
        except Folder.DoesNotExist:
            raise Http404
    def get_objects(self, pk):
        try:
            return Uploads.objects.filter( folder_id= pk)
        except Uploads.DoesNotExist:
            raise Http404

   
    def get(self, request,*args, **kwargs):
        serializer = {}
        folder = self.get_object(self.kwargs.get('folder_id', ''))
        filee = self.get_objects(self.kwargs.get('folder_id', ''))
        serializer['folders'] = FolderSerializer(folder, many=True).data
        serializer['files'] = FileSerializer(filee, many=True).data
        return Response(serializer)



'''                Trash Zone                  '''
class ActivityFolderFileTrashView(APIView):
    serializer_class = ActivitySerializer
    permission_classes = [AllowAny]

    def get_object(self, pk):
        try:
            return Folder.objects.deleted_only()
        except Folder.DoesNotExist:
            raise Http404
    def get_objects(self, pk):
        try:
            return Uploads.objects.deleted_only().filter( folder__id__isnull = False)
        except Uploads.DoesNotExist:
            raise Http404

   
    def get(self, request,*args, **kwargs):
        serializer = {}
        folder = self.get_object(self.kwargs.get('activity_id', ''))
        filee = self.get_objects(self.kwargs.get('activity_id', ''))
        serializer['folders'] = FolderSerializer(folder, many=True).data
        serializer['files'] = FileSerializer(filee, many=True).data
        return Response(serializer)

'''              Undelete / Delete File and folders from Trash        '''

#Trash Files update view
class TrashFilesUpdateView(APIView):
    parser_class = (FileUploadParser,)
    serializer_class = FileSerializer
    permission_classes = [AllowAny]
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
        filee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Trash Folders update view
class TrashFoldersUpdateView(APIView):
    serializer_class = FolderSerializer
    permission_classes = [AllowAny]
    def get_object(self, pk):
        try:
            return Folder.objects.get(pk=pk)
        except Folder.DoesNotExist:
            raise Http404

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
        folder.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def get(self, request, *args, **kwargs):
        folder = self.get_object(self.kwargs.get('folder_id', ''))
        serializer = FolderSerializer(folder)
        return Response(serializer.data)