from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# Create your models here.

from .managers import CustomUserManager


#A model that creates the roles of the users
# class Role(models.Model):
#     '''
#     The Role entries are managed by the system,
#     automatically created via a Django data migration.
#     '''

#     PILLAR_HEAD = 1
#     NORMAL_USER = 2
#     MANAGEMENT_USER = 3
#     ROLE_CHOICES = (
#         (PILLAR_HEAD, 'pillar_head'),
#         (NORMAL_USER, 'normal-user'),
#         (MANAGEMENT_USER, 'management_user'),
        
#     )

#     id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)

#     def __str__(self):
#         return self.get_id_display()

class CustomUser(AbstractBaseUser, PermissionsMixin):
    PILLAR_HEAD = 1
    NORMAL_USER = 2
    MANAGEMENT_USER = 3
    ADMIN = 4
    ROLE_CHOICES = (
        (PILLAR_HEAD, 'pillar_head'),
        (NORMAL_USER, 'normal-user'),
        (MANAGEMENT_USER, 'management_user'),
        (ADMIN, 'admin')
        
    )

    roles = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True, default=2)
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

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    
    contacts =  models.CharField(max_length=30, blank=True, verbose_name = 'Contacts')
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

