from django.contrib import admin
from program.models import *
from dlab.models import Collaborators

# Register your models here.

#create an inline
class CoordinatorInline(admin.StackedInline):
    model = Coordinator
    extra = 1
class FacilitatorInline(admin.StackedInline):
    model = Facilitator
    extra =1
class CollaboratorInline(admin.StackedInline):
    model = Collaborators
    extra =1 

class ActivityAdmin(admin.ModelAdmin):
    inlines = [
        CoordinatorInline,
        FacilitatorInline,
        CollaboratorInline
    ]

admin.site.register(Program)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Venue)

