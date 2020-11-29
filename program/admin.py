from django.contrib import admin
from program.models import *


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

class VenueInline(admin.TabularInline):
    model = Venue
    extra =1  


class ActivityAdmin(admin.ModelAdmin):
    inlines = [
        VenueInline,
        CoordinatorInline,
        FacilitatorInline,
        CollaboratorInline,
        
    ]

admin.site.register(Program)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Venue)

#this method allows you to add a plus button without displaying the Model On Admin Panel
class MyModelAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}
admin.site.register(Venue_detail, MyModelAdmin)