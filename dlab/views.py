from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from dlab.serializers import *
from rest_framework.response import Response
from dlab.models import *
from django.http import Http404
# Create your views here.
'''                       Organizaion  Zone                '''
#view to create and update organization
class OrganizationView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, format=None):
        organizations = Organization.objects.all().order_by("name")
        serializer = OrganizationSerializer(organizations, many=True)
        return Response(serializer.data)
#view to create organization
class AddOrganizationView(APIView):
    serializer_class = OrganizationSerializer
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)
        if valid:
            status_code = status.HTTP_201_CREATED
            serializer.save()
            return Response(serializer.data, status=status_code)

#Retrieve, update or delete a organization instance. 
class OrganizationUpdateView(APIView):
    serializer_class = OrganizationSerializer
    permission_classes = [AllowAny]
    def get_object(self, pk):
        try:
            return Organization.objects.get(pk=pk)
        except Organization.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        organization_key = self.get_object(pk)
        serializer = self.serializer_class(organization_key, data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_201_CREATED
            serializer.save()
            return Response(serializer.data, status=status_code)

    def get(self, request, pk, format=None):
        organization = self.get_object(pk)
        serializer = OrganizationSerializer(organization)
        return Response(serializer.data)


        
'''                       Staff Zone                '''
# List all staffs or create a new one
class StaffView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, format=None):
        staffs = Staff.objects.all()
        serializer = StaffSerializer(staffs, many=True)
        return Response(serializer.data)

class AddStaffView(APIView):
    serializer_class = StaffSerializer
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_201_CREATED
            serializer.save()
            
            return Response(serializer.data, status=status_code)

#Retrieve, update or delete a staff instance. 
class StaffUpdateView(APIView):
    serializer_class = StaffSerializer
    permission_classes = [AllowAny]
    def get_object(self, pk):
        try:
            return Staff.objects.get(pk=pk)
        except Staff.DoesNotExist:
            raise Http404

    def put(self, request, *args, **kwargs):
        staff_key = self.get_object(self.kwargs.get('staff_id', ''))
        serializer = self.serializer_class(staff_key, data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_201_CREATED
            serializer.save()
            return Response(serializer.data, status=status_code)

    def get(self, request, *args, **kwargs):
        staff = self.get_object(self.kwargs.get('staff_id', ''))
        serializer = StaffSerializer(staff)
        return Response(serializer.data)
'''         Profile  zone                '''
#VIew to create and retrieve profiles
class ProfileView(APIView):
    serializer_class = ProfileSerializer
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_201_CREATED
            serializer.save()
            
            return Response(serializer.data, status=status_code)

#Retrieve, update or delete a profile instance. 
class ProfileUpdateView(APIView):
    serializer_class = ProfileSerializer
    permission_classes = [AllowAny]
    def get_object(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            raise Http404

    def put(self, request, *args, **kwargs):
        profile_key = self.get_object(self.kwargs.get('profile_id', ''))
        serializer = self.serializer_class(profile_key, data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_201_CREATED
            serializer.save()
            return Response(serializer.data, status=status_code)

    def get(self, request, *args, **kwargs):
        profile = self.get_object(self.kwargs.get('profile_id', ''))
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

'''            StaffProfile Zone           '''
class StaffProfileView(APIView):
    serializer_class = StaffSerializer
    permission_classes = [AllowAny]

    def get_object(self, pk):
        try:
            return Profile.objects.filter( user_staff_id= pk)
        except Profile.DoesNotExist:
            raise Http404

   
    def get(self, request,*args, **kwargs):
        profile = self.get_object(self.kwargs.get('staff_id', ''))
        serializer = ProfileSerializer(profile, many=True)
        return Response(serializer.data)