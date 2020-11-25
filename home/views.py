from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from account.serializers import UserLoginSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated


from .serializers import HomeSerializer

class DlabHome(View):
    serializer_class = HomeSerializer
    permission_classes = [IsAuthenticated]
    def get(self, request):
        # <view logic>
        # response = {
               
        #         'message': 'User logged in successfully',
        #         'access': serializer.data['access'],
        #         'refresh': serializer.data['refresh'],
        #         'authenticatedUser': {
        #             'email': serializer.data['email'],
        #             'role': serializer.data['role'],
        #             'pillar':serializer.data['pillars']
        #         }
        # }
        
        return render(request, 'templates/homePage.html')