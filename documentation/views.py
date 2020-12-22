from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from program.serializers import ActivitySerializer
from documentation.serializers import *
from rest_framework.response import Response
from documentation.models import Uploads
# Create your views here.
class UploadsView(APIView):
    serializer_class = ActivitySerializer
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_200_OK
            #make a query to return all the documentation of a particular activity
            uploads = Uploads.objects.filter(activity_name__id = serializer.data['id'])
            uploads = UploadsSerializer(uploads, many=True).data
            response = uploads
            return Response(response, status=status_code)