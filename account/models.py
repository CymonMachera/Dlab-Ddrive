from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# Create your models here.

from .managers import CustomUserManager

class CustomUser(AbstractBaseUser, PermissionsMixin):
    PILLAR_HEAD = 3
    NORMAL_USER = 4
    MANAGEMENT_USER = 2
    ADMIN = 1
    ROLE_CHOICES = (
        (PILLAR_HEAD, 'Pillar Head'),
        (NORMAL_USER, 'Normal User'),
        (MANAGEMENT_USER, 'Management user'),
        (ADMIN, 'Admin')
        
    )

    roles = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True, default=4)
    email = models.EmailField(max_length = 40, verbose_name = 'Email Address', unique = True)
    first_name =  models.CharField(max_length=30, blank=True, verbose_name = 'First Name')
    last_name =  models.CharField(max_length=30, blank=True, verbose_name = 'Last Name')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()
    
    REQUIRED_FIELDS = ['first_name', 'last_name']
    
    USERNAME_FIELD = 'email'

    EMAIL_FIELD = 'email'

    def __str__(self):
        return self.email

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name
    class Meta:
        verbose_name_plural = "Users"
   
    
class Pillar(models.Model):
    name = models.CharField(max_length=50, blank = False, verbose_name = "Enter pillar Name")
    pillar_desc = models.TextField(max_length=500, blank=True)
    user_pillar = models.ManyToManyField(CustomUser, verbose_name = "Add Members", related_name = "pillar",)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Pillars"
    