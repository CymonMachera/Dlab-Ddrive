from django.db import models
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE_CASCADE
from documentation.manager import *
from datetime import datetime
from django.urls import reverse
from django.utils.text import slugify
from account.models import CustomUser
from program.models import Activity
# Create your models here.
#a model to create the folder
class Folder(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE
    objects = MyModelManager()

    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    activity_name = models.ForeignKey(Activity, on_delete=models.CASCADE, blank = True, null=True)
    name = models.CharField(max_length=64)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    path = models.CharField(max_length=2048, blank=True)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        kwargs = {'slug' : self.slug}
        return reverse('', kwargs=kwargs)

    def get_path(self):
        if self.parent: 
            yield from self.parent.get_path()
        yield self.name

        
    def complete_get_path(self):
        return "/".join(self.get_path())

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.path = self.complete_get_path()
        return super().save(*args, **kwargs)


    class Meta:
        unique_together = [['parent', 'name']]
        ordering = ('name',)

class Uploads(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE
    objects = MyModelManager()

    Images = 3
    Video = 2
    Documents = 1
    ROLE_CHOICES = (
        (Images, 'Images'),
        (Video, 'Video'),
        (Documents, 'Documents')
        
    )
    activity_name = models.ForeignKey(Activity, on_delete=models.CASCADE, blank = True, null=True)
    doc_type = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=False)
    doc_name = models.CharField(max_length=50)
    uploader_name = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, blank = True, null=True)
    dete_uploaded = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    #prepare the url
    url = str(folder.name)
    
    upload_path = models.FileField(upload_to=url, default = "pillar/", verbose_name = "Choose File", blank = False)


    def __str__(self):
        return self.doc_name

    class Meta:
        verbose_name_plural = "Documentations"
