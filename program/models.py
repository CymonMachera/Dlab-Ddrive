from django.db import models
from account.models import Pillar
from dlab.models import Organization, Staff
# Create your models here.
class Program(models.Model):
    name = models.CharField(max_length=50, blank = False, verbose_name = "Program or Project Name")
    Pillar = models.ForeignKey(Pillar, on_delete = models.CASCADE)
    program_desc = models.TextField(max_length=500, blank=True, verbose_name = "Program Description")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Programs And Projects"

class Location(models.Model):
    location = models.CharField(max_length=50, blank = False)

#this model will only store venue details
class Venue_detail(models.Model):
    name = models.CharField(max_length=50, blank = False, verbose_name = "Venue Name")
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Venues"

        


class Activity(models.Model):
    Workshop = 'Workshop'
    Round_Table = 'Round Table'
    Training = 'Training'
    ROLE_CHOICES = (
        (Workshop, 'Workshop'),
        (Round_Table, 'Round Table'),
        (Training, 'Training')
        
    )

    
    name = models.CharField(max_length=50, blank = False, verbose_name = "Activity Name")
    activity_Program_type = models.ForeignKey(Program, on_delete = models.CASCADE, verbose_name = "Program/Project Name")
    type_of_activity = models.CharField(choices=ROLE_CHOICES, blank=True, null=False, max_length = 20)
    Participants_number = models.IntegerField(blank=False, verbose_name = "Number Of Participants")
    Start_time = models.DateField(blank = False, editable=True, verbose_name = "Start Date")
    End_time = models.DateField(blank = False, editable=True, verbose_name = "End Date")
    program_desc = models.TextField(max_length=500, blank=True, verbose_name = "Activity Description")
    
    def __str__(self):
        return self.name

class Collaborators(models.Model):
    collaborator_name = models.ForeignKey(Staff, on_delete=models.CASCADE)
    Role =  models.CharField(max_length=50, blank = False, verbose_name = "Collaboration Role")
    activity = models.ForeignKey(Activity, on_delete = models.CASCADE)

    def __str__(self):
        name = str(self.collaborator_name)
        role = self.Role
        return name + "  ----->  " + role

class Coordinator(models.Model):
    name = models.ForeignKey(Staff, on_delete=models.CASCADE)
    # organization = models.ForeignKey(self.name.organization, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete = models.CASCADE)
    def __str__(self):
        return str(self.name)

class Facilitator(models.Model):
    name = models.ForeignKey(Staff, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete = models.CASCADE)
    def __str__(self):
        return str(self.name) + str()


#this model will use the model venue_details in addition to desplaying time 
class Venue(models.Model):
    name = models.ForeignKey(Venue_detail, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete = models.CASCADE)
    Start_time = models.DateTimeField(blank = False, editable=True)
    End_time = models.DateTimeField(blank = False, editable=True)
    
    def __str__(self):
        full_detail = '%s %s  %s %s' % (str(self.name), str(self.Start_time), str(self.End_time), str(self.activity))
        return full_detail.strip()

    class Meta:
        verbose_name_plural = "Venue Usage"
