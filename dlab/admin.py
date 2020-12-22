from django.contrib import admin
from dlab.models import *
from program.models import Collaborators

#crate the profile inline 
class ProfileInline(admin.StackedInline):
    model = Profile
    verbose_name_plural = 'Profile'


class StaffAdmin(admin.ModelAdmin):
    search_fields = ('first_name','last_name',)
    inlines = [
        ProfileInline,
    ]
    filter_horizontal = ('organization', )

admin.site.register(Organization)
admin.site.register(Staff, StaffAdmin)


