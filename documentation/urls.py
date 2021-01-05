from django.urls import path
from django.conf.urls import url
from .views import *

urlpatterns = [

    # level 1
    path('', ActivityFolderFileView.as_view(), name='files'),
    path('addfile/', AddFileView.as_view(), name='add_file'),
    path('<int:file_id>/', FileUpdateView.as_view(), name='file_update'),

    path('addfolder/', AddFolderView.as_view(), name='add_folder'),
    path('folder/<int:folder_id>/', FolderUpdateView.as_view(), name='folder_update'),
    
    #level 2
    path('folder/<int:folder_id>/files/', FolderFileView.as_view(), name='files'),
    path('folder/<int:folder_id>/files/addfile/', AddFileView.as_view(), name='add_file'),
    path('folder/<int:folder_id>/files/<int:file_id>/', FileUpdateView.as_view(), name='file_update'),

    path('folder/<int:folder_id>/files/addfolder/', AddFolderView.as_view(), name='add_folder'),
    path('folder/<int:folder_id>/files/folder/<int:folder_level2_id>/', FolderLevel2UpdateView.as_view(), name='folder_update'),
    
   
]