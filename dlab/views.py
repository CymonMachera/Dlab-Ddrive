from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from account.serializers import UserLoginSerializer
from rest_framework.permissions import AllowAny

class DlabLogin(View):
    serializer_class = UserLoginSerializer
    permission_classes = (AllowAny, )
    def get(self, request):
        # <view logic>
        

        
        return render(request, 'templates/login.html')
