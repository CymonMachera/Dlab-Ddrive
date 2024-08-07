from django.shortcuts import render
from rest_framework import generics

from .models import Advertisement
from .serializers import AdvertisementSerializer
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        response = super(StandardResultsSetPagination,
                         self).get_paginated_response(data)
        response.data['total_pages'] = self.page.paginator.num_pages
        if self.page_query_param:
            response.data['page_size'] = self.page.paginator.per_page
        else:
            response.data['page_size'] = self.page_size
        return response
# Create your views here.
class AdverisementView(generics.ListCreateAPIView):
    serializer_class = AdvertisementSerializer
    permission_classes = [AllowAny]
    queryset = Advertisement.objects.all()