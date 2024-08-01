from django.db import models

class Advertisement(models.Model):
    title = models.CharField(max_length=50, blank = False)
    description = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to="advertisement/%Y/%m/%d/", verbose_name = "Choose File", blank = False)
    event_date = models.DateField()

    def __str__(self):
        return self.title
