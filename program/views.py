from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from .serializers import ProgramSerializer
from rest_framework.response import Response
from program.models import Program

class ProgramView(APIView):
    serializer_class = ProgramSerializer
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_200_OK
            #make a query to return programs belonging to a particular pillar
            programs = Program.objects.filter(Pillar__name = serializer.data['name'])
            programs = ProgramSerializer(programs, many=True).data
            programs = [f['name'] for f in programs]
            response = {
            'statusCode': status_code, 
            'programs' : programs
            }
            return Response(response, status=status_code)

         


            
       