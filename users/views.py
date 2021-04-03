from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from safedelete.models import HARD_DELETE
from django.http import Http404
from account.models import CustomUser
from users.serializer import *
from rest_framework.response import Response

# Create your views here.
'''          User Zone     '''
 # this view takes in the   
class UserView(APIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        user = CustomUser.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

#Retrieve a user instance. 
class UserUpdateView(APIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
