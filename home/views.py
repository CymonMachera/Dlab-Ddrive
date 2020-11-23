from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from account.serializers import UserLoginSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated

class DlabHome(View):
    serializer_class = UserLoginSerializer
    permission_classes = (IsAuthenticated, )
    def get(self, request):
        # <view logic>
        
        return render(request, 'templates/homePage.html')