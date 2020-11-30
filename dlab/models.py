from django.db import models
from account.models import CustomUser

class Organization(models.Model):
    name = models.CharField(max_length=50, blank = False, verbose_name = "Organization Name")
    Address = models.CharField(max_length=50, blank = False)
    Telephone_number = models.CharField(max_length=50, blank = False)
    Email = models.EmailField( max_length=254)
    Description = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.name

class Staff(models.Model):
    first_name =  models.CharField(max_length=30, blank=False, verbose_name = 'First Name')
    last_name =  models.CharField(max_length=30, blank=False, verbose_name = 'Last Name') 
    organization = models.ManyToManyField(Organization, verbose_name = "Organization", related_name = "staff")

    def __str__(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()



class Profile(models.Model):
    user_staff = models.OneToOneField(Staff, on_delete=models.CASCADE)
    Title = models.CharField(max_length=50, blank = True, verbose_name = "Title")
    Telephone_number =  models.CharField(max_length=30, blank=True, verbose_name = 'Contacts')
    email = models.EmailField( max_length=254, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    Address = models.CharField(max_length=30, blank=True)
    biography = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.Title  #check this part for concistance
