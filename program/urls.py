from django.urls import path
from django.conf.urls import url
from .views import ProgramView

urlpatterns = [
    path('', ProgramView.as_view(), name='programs'),
    
]