from django.urls import path
from django.conf.urls import url
from trash.views import *

urlpatterns = [
 #trash level 1
    path('', UserView.as_view(), name='Users'),
    path('<int:pk>/', UserUpdateView.as_view(), name='User retrieve'),
    path('<int:pk>/trash/', UserFolderFileTrashView.as_view(), name='Trash folder_files'),
    path('<int:pk>/trash/folder/<int:folder_id>/', TrashFoldersUpdateView.as_view(), name='Trash_folder_update'),
    path('<int:pk>/trash/file/<int:file_id>/', TrashFilesUpdateView.as_view(), name='Trash_file_update'),

]