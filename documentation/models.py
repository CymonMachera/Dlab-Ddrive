import os
import safedelete
from django.db import models
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE_CASCADE
from safedelete.models import HARD_DELETE
from documentation.manager import *
from datetime import datetime
from django.urls import reverse
from django.utils.text import slugify
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from account.models import CustomUser
from program.models import Activity, Program
# Create your models here.
#a model to create the folder
class Folder(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE
    objects = MyModelManager()

    creator = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null = True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, blank = True, null=True)
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
    CHOICES = (
        (Images, 'Images'),
        (Video, 'Video'),
        (Documents, 'Documents')
        
    )
    program = models.ForeignKey(Program, on_delete=models.CASCADE, blank = True, null=True)
    doc_type = models.PositiveSmallIntegerField(choices=CHOICES, blank=True, null=False)
    doc_name = models.CharField(max_length=50)
    uploader_name = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, blank = True, null=True)
    dete_uploaded = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    upload_path = models.FileField(upload_to="uploads/%Y/%m/%d/", default = "pillar/", verbose_name = "Choose File", blank = False)


    def __str__(self):
        return self.doc_name

    class Meta:
        verbose_name_plural = "Files"


# These two auto-delete files from filesystem when they are unneeded:

@receiver(models.signals.post_delete, sender=Uploads)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `Uploads` object is deleted.
    """
    if instance.upload_path:
        if os.path.isfile(instance.upload_path.path):
            os.remove(instance.upload_path.path)

@receiver(models.signals.pre_save, sender=Uploads)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `Uploads` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = Uploads.objects.get(pk=instance.pk).upload_path
    except Uploads.DoesNotExist:
        return False

    new_file = instance.upload_path
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)

