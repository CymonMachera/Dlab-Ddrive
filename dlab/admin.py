from django.contrib import admin
from dlab.models import *
from program.models import Collaborators

#crate the profile inline 
class ProfileInline(admin.StackedInline):
    model = Profile
    verbose_name_plural = 'Profile'


class StaffAdmin(admin.ModelAdmin):
    inlines = [
        ProfileInline,
    ]

admin.site.register(Collaborators)
admin.site.register(Organization)
admin.site.register(Staff, StaffAdmin)


