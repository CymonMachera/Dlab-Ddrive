from django.urls import path
from django.conf.urls import url
from .views import *

urlpatterns = [
    path('', ActivityFolderFileView.as_view(), name='files'),

    #''' model these things to reflect the the above '''
    path('addfile/', AddFileView.as_view(), name='add_file'),
    path('<int:file_id>/', FileUpdateView.as_view(), name='file_update'),

    path('addfolder/', AddFolderView.as_view(), name='add_folder'),
    path('folder/<int:folder_id>/', FolderUpdateView.as_view(), name='folder_update'),
    
    path('folder/<int:folder_id>/files/', FolderFileView.as_view(), name='folder_update'),
    path('folder/<int:folder_id>/files/addfile/', AddFileView.as_view(), name='add_file'),
    path('folder/<int:folder_id>/files/<int:file_id>/', FileUpdateView.as_view(), name='file_update'),

    
   
]