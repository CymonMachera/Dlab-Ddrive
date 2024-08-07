
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from django.shortcuts import redirect

from .serializers import UserLoginSerializer

from .models import CustomUser, Pillar


# Create your views here.
class UserLoginView(APIView):
    serializer_class = UserLoginSerializer
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_200_OK
            
            # fetch pillar names
            pillar_names = Pillar.objects.filter(user_pillar=serializer.data['id']).values_list('name', flat=True)
            pillar_names_list = list(pillar_names)

            
            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'User logged in successfully',
                'access': serializer.data['access'],
                'refresh': serializer.data['refresh'],
                'authenticatedUser': {
                    'email': serializer.data['email'],
                    'role': serializer.data['role'],
                    'pillar':serializer.data['pillars'],
                    'name' : serializer.data['name'],
                    'designation' : serializer.data['designation'],
                    'id': serializer.data['id'],
                    'pillars': pillar_names_list
                    
                }
            }

            return Response(response, status=status_code)
       