from django.db import models
from account.models import CustomUser
from program.models import Activity
# Create your models here.
class Uploads(models.Model):
    Images = 3
    Video = 2
    Documents = 1
    ROLE_CHOICES = (
        (Images, 'Images'),
        (Video, 'Video'),
        (Documents, 'Documents')
        
    )
    activity_name = models.ForeignKey(Activity, on_delete=models.CASCADE)
    doc_name = models.CharField(max_length=50)
    uploader_name = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    doc_type = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=False)
    dete_uploaded = models.DateTimeField(auto_now_add=True)
    upload_path = models.FileField(upload_to="pillar", verbose_name = "Choose File")

    def __str__(self):
        return str(self.doc_name)

    class Meta:
        verbose_name_plural = "Documentations"
