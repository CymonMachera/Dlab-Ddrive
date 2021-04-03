from django.urls import path
from django.conf.urls import url
from trash.views import *

urlpatterns = [
 #trash level 1
    path('', UserFolderFileTrashView.as_view(), name='Trash folder_files'),
    path('folder/<int:folder_id>/', TrashFoldersUpdateView.as_view(), name='Trash_folder_update'),
    path('file/<int:file_id>/', TrashFilesUpdateView.as_view(), name='Trash_file_update'),

]