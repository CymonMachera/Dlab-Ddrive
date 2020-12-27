from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from .serializers import *
from rest_framework.response import Response
from program.models import Program, Activity

 # this view takes in the   
class PillarView(APIView):
    serializer_class = PillarSerializer
    permission_classes = [AllowAny]
    def get(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_200_OK
            #make a query to return list of pillars 
            pillar = Pillar.objects.all()
            pillar = ActivitySerializer(pillar, many=True).data
            response = pillar
            return Response(response, status=status_code)

class ProgramView(APIView):
    serializer_class = PillarProgramSerializer
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_200_OK
            #make a query to return programs belonging to a particular pillar
            programs = Program.objects.filter(Pillar__name = serializer.data['name'])
            programs = ProgramSerializer(programs, many=True).data
            response = programs
            return Response(response, status=status_code)

   
class ActivityView(APIView):
    serializer_class = ProgramSerializer
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_200_OK
            #make a query to return activity belonging to a particular program
            activity = Activity.objects.filter(activity_Program_type__id = serializer.data['id'])
            activity = ActivitySerializer(activity, many=True).data
            response = activity
            return Response(response, status=status_code)


class VenueView(APIView):
    serializer_class = VenueSerializer
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_201_CREATED
            serializer.save()
            return Response(serializer.data, status=status_code)
class VenueRegisterView(APIView):
    serializer_class = VenueDetailSerializer
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_201_CREATED
            serializer.save()
            
            return Response(serializer.data, status=status_code)

class LocationView(APIView):
    serializer_class = LocationSerializer
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_201_CREATED
            serializer.save()
            return Response(serializer.data, status=status_code)








       