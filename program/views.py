from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import *
from django.http import Http404
from rest_framework.response import Response
from program.models import Program, Activity

'''          Pillar Zone     '''
 # this view takes in the   
class PillarView(APIView):
    serializer_class = PillarSerializer
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        pillar = Pillar.objects.all()
        serializer = PillarSerializer(pillar, many=True)
        return Response(serializer.data)
#Retrieve, update or delete a pillar instance. 
class PillarUpdateView(APIView):
    serializer_class = PillarSerializer
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Pillar.objects.get(pk=pk)
        except Pillar.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):
        pillar = self.get_object(pk)
        serializer = PillarSerializer(pillar)
        return Response(serializer.data)

'''        PillarProgram zone        '''
class PillarProgramView(APIView):
    serializer_class = PillarSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Program.objects.filter(Pillar__id = pk).order_by('-date_modified')
        except Program.DoesNotExist:
            raise Http404

   
    def get(self, request, pk, format=None):
        programs = self.get_object(pk)
        serializer = ProgramSerializer(programs, many=True)
        return Response(serializer.data)


'''            Program/project Zone          '''
class ProgramView(APIView):
    serializer_class = ProgramSerializer
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)
        if valid:
            status_code = status.HTTP_201_CREATED
            serializer.save()
            return Response(serializer.data, status=status_code)
   
#Retrieve, update or delete a program instance. 
class ProgramUpdateView(APIView):
    serializer_class = ProgramSerializer
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Program.objects.get(pk=pk)
        except Program.DoesNotExist:
            raise Http404

    def put(self, request, *args, **kwargs):
        program_key = self.get_object(self.kwargs.get('pk_alt', ''))
        serializer = self.serializer_class(program_key, data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_201_CREATED
            serializer.save()
            return Response(serializer.data, status=status_code)

    def get(self, request, *args, **kwargs):
        program = self.get_object(self.kwargs.get('pk_alt', ''))
        serializer = ProgramSerializer(program)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        program = self.get_object(pk)
        program.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


'''            ProgramActivity Zone           '''
class ProgramActivityView(APIView):
    serializer_class = ProgramSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Activity.objects.filter( activity_Program_type_id= pk)
        except Activity.DoesNotExist:
            raise Http404

   
    def get(self, request,*args, **kwargs):
        programs = self.get_object(self.kwargs.get('pk_alt', ''))
        serializer = ActivitySerializer(programs, many=True)
        return Response(serializer.data)



'''            Activity Zone          '''
class ActivityView(APIView):
    serializer_class = ActivitySerializer
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)
        if valid:
            status_code = status.HTTP_201_CREATED
            serializer.save()
            return Response(serializer.data, status=status_code)
   
#Retrieve, update or delete a activity instance. 
class ActivityUpdateView(APIView):
    serializer_class = ActivitySerializer
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Activity.objects.get(pk=pk)
        except Activity.DoesNotExist:
            raise Http404

    def put(self, request, *args, **kwargs):
        activity_key = self.get_object(self.kwargs.get('activity_id', ''))
        serializer = self.serializer_class(activity_key, data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_201_CREATED
            serializer.save()
            return Response(serializer.data, status=status_code)

    def get(self, request, *args, **kwargs):
        activity = self.get_object(self.kwargs.get('activity_id', ''))
        serializer = ActivitySerializer(activity)
        return Response(serializer.data)
    
    def delete(self, request, pk, format=None):
        activity = self.get_object(pk)
        activity.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


'''            New venue register          '''
class AddVenueView(APIView):
    serializer_class = VenueSerializer
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)
        if valid:
            status_code = status.HTTP_201_CREATED
            serializer.save()
            return Response(serializer.data, status=status_code)
class VenueView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        venue = Venue_detail.objects.all()
        serializer = VenueSerializer(venue, many=True)
        return Response(serializer.data)
#Retrieve, update or delete a venue instance. 
class VenueUpdateView(APIView):
    serializer_class = VenueSerializer
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Venue_detail.objects.get(pk=pk)
        except Venue_detail.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        Venue_Detail_key = self.get_object(pk)
        serializer = self.serializer_class(Venue_Detail_key, data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_201_CREATED
            serializer.save()
            return Response(serializer.data, status=status_code)

    def get(self, request, pk, format=None):
        venue_detail = self.get_object(pk)
        serializer = VenueSerializer(venue_detail)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        venue_detail = self.get_object(pk)
        venue_detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

'''        Venue  usage Zone         '''
class VenueUsageView(APIView):
    ''' currently not in use, later used to display all venue usages'''
    def get(self, request, format=None):
        venue = Venue.objects.all()
        serializer = VenueUsageSerializer(venue, many=True)
        return Response(serializer.data)

class AddVenueUsageView(APIView):
    serializer_class = VenueUsageSerializer
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)
        if valid:
            status_code = status.HTTP_201_CREATED
            serializer.save()
            return Response(serializer.data, status=status_code)
#Retrieve, update or delete a venue usage instance. 
class VenueUsageUpdateView(APIView):
    serializer_class = VenueUsageSerializer
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Venue.objects.get(pk=pk)
        except Venue.DoesNotExist:
            raise Http404

    def put(self, request, *args, **kwargs):
        Venue_key = self.get_object(self.kwargs.get('venueusage_id', ''))
        serializer = self.serializer_class(Venue_key, data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_201_CREATED
            serializer.save()
            return Response(serializer.data, status=status_code)

    def get(self, request, *args, **kwargs):
        venue = self.get_object(self.kwargs.get('venueusage_id', ''))
        serializer = VenueUsageSerializer(venue)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        venue = self.get_object(self.kwargs.get('venueusage_id', ''))
        venue.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

'''          Loction Registration Zone             '''
class LocationView(APIView):
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_201_CREATED
            serializer.save()
            return Response(serializer.data, status=status_code)
    
    def get(self, request, format=None):
        location = Location.objects.all()
        serializer = LocationSerializer(location, many=True)
        return Response(serializer.data)

#Retrieve, update or delete a location instance. 
class LocationUpdateView(APIView):
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Location.objects.get(pk=pk)
        except Location.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        location_key = self.get_object(pk)
        serializer = self.serializer_class(location_key, data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_201_CREATED
            serializer.save()
            return Response(serializer.data, status=status_code)

    def get(self, request, pk, format=None):
        location = self.get_object(pk)
        serializer = LocationSerializer(location)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        location = self.get_object(pk)
        location.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


'''          Coordinator  Zone             '''
class CoordinatorView(APIView):
    serializer_class = CoordinatorSerializer
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_201_CREATED
            serializer.save()
            return Response(serializer.data, status=status_code)

#Retrieve, update or delete a coordinator instance. 
class CoordinatorUpdateView(APIView):
    serializer_class = CoordinatorSerializer
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Coordinator.objects.get(pk=pk)
        except Coordinator.DoesNotExist:
            raise Http404

    def put(self, request, *args, **kwargs):
        coordinator_key = self.get_object(self.kwargs.get('coordinator_id', ''))
        serializer = self.serializer_class(coordinator_key, data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_201_CREATED
            serializer.save()
            return Response(serializer.data, status=status_code)

    def get(self, request, *args, **kwargs):
        coordinator = self.get_object(self.kwargs.get('coordinator_id', ''))
        serializer = CoordinatorSerializer(coordinator)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        coordinator = self.get_object(self.kwargs.get('coordinator_id', ''))
        coordinator.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


'''          Collaborator  Zone             '''
class CollaboratorsView(APIView):
    serializer_class = CollaboratorsSerializer
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_201_CREATED
            serializer.save()
            return Response(serializer.data, status=status_code)
    

#Retrieve, update or delete a coordinator instance. 
class CollaboratorsUpdateView(APIView):
    serializer_class = CollaboratorsSerializer
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Collaborators.objects.get(pk=pk)
        except Collaborators.DoesNotExist:
            raise Http404

    def put(self, request, *args, **kwargs):
        coordinator_key = self.get_object(self.kwargs.get('collaborator_id', ''))
        serializer = self.serializer_class(coordinator_key, data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_201_CREATED
            serializer.save()
            return Response(serializer.data, status=status_code)

    def get(self, request, *args, **kwargs):
        collaborator = self.get_object(self.kwargs.get('collaborator_id', ''))
        serializer = CollaboratorsSerializer(collaborator)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        collaborator = self.get_object(self.kwargs.get('collaborator_id', ''))
        collaborator.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

'''          Facilitator  Zone             '''
class FacilitatorView(APIView):
    serializer_class = FacilitatorSerializer
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_201_CREATED
            serializer.save()
            return Response(serializer.data, status=status_code)
    

#Retrieve, update or delete a coordinator instance. 
class FacilitatorUpdateView(APIView):
    serializer_class = FacilitatorSerializer
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Facilitator.objects.get(pk=pk)
        except Facilitator.DoesNotExist:
            raise Http404

    def put(self, request, *args, **kwargs):
        facilitator_key = self.get_object(self.kwargs.get('facilitator_id', ''))
        serializer = self.serializer_class(facilitator_key, data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_201_CREATED
            serializer.save()
            return Response(serializer.data, status=status_code)

    def get(self, request, *args, **kwargs):
        facilitator = self.get_object(self.kwargs.get('facilitator_id', ''))
        serializer = FacilitatorSerializer(facilitator)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        facilitator = self.get_object(self.kwargs.get('facilitator_id', ''))
        facilitator.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

       
###################################
'''            ActivityCoordiantor Zone           '''
class ActivityCoordinatorView(APIView):
    serializer_class = ActivitySerializer
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Coordinator.objects.filter( activity_id= pk)
        except Coordinator.DoesNotExist:
            raise Http404

   
    def get(self, request,*args, **kwargs):
        coordinator = self.get_object(self.kwargs.get('activity_id', ''))
        serializer = CoordinatorSerializer(coordinator, many=True)
        return Response(serializer.data)

'''            ActivityCollaborator Zone           '''
class ActivityCollaboratorsView(APIView):
    serializer_class = ActivitySerializer
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Collaborators.objects.filter( activity_id= pk)
        except Collaborators.DoesNotExist:
            raise Http404

   
    def get(self, request,*args, **kwargs):
        collaborator = self.get_object(self.kwargs.get('activity_id', ''))
        serializer = CollaboratorsSerializer(collaborator, many=True)
        return Response(serializer.data)

'''            ActivityFacillitator Zone           '''
class ActivityFacilitatorView(APIView):
    serializer_class = ActivitySerializer
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Facilitator.objects.filter( activity_id= pk)
        except Facilitator.DoesNotExist:
            raise Http404

   
    def get(self, request,*args, **kwargs):
        facilitator = self.get_object(self.kwargs.get('activity_id', ''))
        serializer = FacilitatorSerializer(facilitator, many=True)
        return Response(serializer.data)

'''            ActivityVenueUSage Zone           '''
class ActivityVenueUsageView(APIView):
    serializer_class = ActivitySerializer
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Venue.objects.filter( activity_id= pk)
        except Venue.DoesNotExist:
            raise Http404

   
    def get(self, request,*args, **kwargs):
        venuusage = self.get_object(self.kwargs.get('activity_id', ''))
        serializer = VenueUsageSerializer(venuusage, many=True)
        return Response(serializer.data)