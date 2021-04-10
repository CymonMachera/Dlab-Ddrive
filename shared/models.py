from django.db import models
from documentation.models import Folder, Uploads
from account.models import CustomUser

# Create your models here.
class SharedFolder(models.Model):
    shared_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    shared_to = models.ManyToManyField(CustomUser, related_name = "shared_folder")
    date_shared = models.DateTimeField(auto_now_add=True)
    folder_link  = models.CharField(max_length = 100, blank = False, null = False, default = None)
    pillar_id  = models.CharField(max_length = 2, blank = False, null = False, default = None)
    program_id  = models.CharField(max_length = 20, blank = False, null = False, default = None)
    activity_id  = models.CharField(max_length = 20, blank = False, null = False, default = None)


    def __str__(self):
        return self.folder_link

class SharedFile(models.Model):
    shared_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    shared_to = models.ManyToManyField(CustomUser, related_name = "shared_file")
    date_shared = models.DateTimeField(auto_now_add=True)
    file_link  = models.CharField(max_length = 100, blank = False, null = False, default = None)

    def __str__(self):
        return self.file_link