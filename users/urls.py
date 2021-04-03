from django.urls import path, include
from django.conf.urls import url
from users.views import *

urlpatterns = [
 #trash level 1
    path('', UserView.as_view(), name='Users'),
    path('<int:pk>/', UserUpdateView.as_view(), name='User retrieve'),
    
    #include url from shared
    path('<int:pk>/shared/', include('shared.urls')),

    #include url from trash
    path('<int:pk>/trash/', include('trash.urls')),

]