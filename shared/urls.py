from django.urls import path
from django.conf.urls import url
from shared.views import *

urlpatterns = [
 #trash level 1
    path('', UserSharedFolderFileView.as_view(), name='shared folder_files'), #  used on the shared button

    path('addSharedFile/', AddSharedFileView.as_view(), name='add shared file'),  # Add a shared file (By user owning a file)
    path('file/<int:file_id>/', SharedFileUpdateView.as_view(), name='Shared_file_update'),
    
    path('addSharedFolder/', AddSharedFolderView.as_view(), name='add shared folder'), # Add a shared folder (By user owning a folder)
    path('folder/<int:folder_id>/', SharedFolderUpdateView.as_view(), name='Shared_folder_update'),
]