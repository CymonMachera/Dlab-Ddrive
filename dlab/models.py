from django.db import models
from program.models import Activity

class Organization(models.Model):
    name = models.CharField(max_length=50, blank = False, verbose_name = "Organization Name")
    Address = models.CharField(max_length=50, blank = False)
    Telephone_number = models.CharField(max_length=50, blank = False)
    Email = models.EmailField( max_length=254)
    Description = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.name
class Collaborators(models.Model):
    collaborator_name = models.ForeignKey(Organization, on_delete=models.CASCADE)
    Role =  models.CharField(max_length=50, blank = False, verbose_name = "Collaboration Role")
    activity = models.ForeignKey(Activity, on_delete = models.CASCADE)

    def __str__(self):
        name = str(self.collaborator_name)
        role = self.Role
        return name + "  ----->  " + role