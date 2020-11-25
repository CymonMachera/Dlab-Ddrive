from django.db import models
from account.models import Pillar
# Create your models here.
class Program(models.Model):
    name = models.CharField(max_length=50, blank = False, verbose_name = "Program or Project Name")
    Pillar = models.ForeignKey(Pillar, on_delete = models.CASCADE)
    program_desc = models.TextField(max_length=500, blank=True, verbose_name = "Program Description")
    def __str__(self):
        return self.name


class Venue(models.Model):
    name = models.CharField(max_length=50, blank = False, verbose_name = "Venue Name")
    location = models.CharField(max_length=50, blank = False)
    Start_time = models.DateTimeField(blank = False, editable=True)
    End_time = models.DateTimeField(blank = False, editable=True)

    def __str__(self):
        return self.name


class Activity(models.Model):
    name = models.CharField(max_length=50, blank = False, verbose_name = "Activity Name")
    activity_Program_type = models.ForeignKey(Program, on_delete = models.CASCADE)
    Participants_number = models.IntegerField(blank=False)
    Start_time = models.DateTimeField(blank = False, editable=True, verbose_name = "Start Date")
    End_time = models.DateTimeField(blank = False, editable=True, verbose_name = "End Date")
    program_desc = models.TextField(max_length=500, blank=True, verbose_name = "Activity Description")
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, editable = True)
    

    def __str__(self):
        return self.name

class Coordinator(models.Model):
    name = models.CharField(max_length=50)
    activity = models.ForeignKey(Activity, on_delete = models.CASCADE)
    def __str__(self):
        return self.name

class Facilitator(models.Model):
    name = models.CharField(max_length=50)
    activity = models.ForeignKey(Activity, on_delete = models.CASCADE)
    def __str__(self):
        return self.name
