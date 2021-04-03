from django.db import models
from documentation.models import Folder, Uploads
from account.models import CustomUser

# Create your models here.
class SharedFolder(models.Model):
    shared_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    shared_to = models.ManyToManyField(CustomUser, related_name = "shared_folder")
    date_shared = models.DateTimeField(auto_now_add=True)
    folder_id  = models.ForeignKey(Folder, on_delete=models.CASCADE)


    def __str__(self):
        return self.folder_id

class SharedFile(models.Model):
    shared_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    shared_to = models.ManyToManyField(CustomUser, related_name = "shared_file")
    date_shared = models.DateTimeField(auto_now_add=True)
    file_id  = models.ForeignKey(Uploads, on_delete=models.CASCADE)


    def __str__(self):
        return self.file_id