# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Activity(models.Model):
    activity_id = models.IntegerField(primary_key=True)
    program_id = models.IntegerField(blank=True, null=True)
    start_date = models.CharField(max_length=50, blank=True, null=True)
    end_date = models.CharField(max_length=50, blank=True, null=True)
    start_time = models.CharField(max_length=50, blank=True, null=True)
    end_time = models.CharField(max_length=50, blank=True, null=True)
    no_of_participants = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'activity'


class ActivityCoordinator(models.Model):
    coordinator = models.CharField(primary_key=True, max_length=50)
    activity_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'activity_coordinator'


class ActivityDesc(models.Model):
    name = models.CharField(primary_key=True, max_length=50)
    activity_id = models.IntegerField()
    type_of_activity = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'activity_desc'


class ActivityFacilitator(models.Model):
    facilitator = models.CharField(primary_key=True, max_length=50)
    activity_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'activity_facilitator'


class ActualDocumentation(models.Model):
    actual_document = models.TextField()
    documentation_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'actual_documentation'


class Collaborator(models.Model):
    colab_id = models.IntegerField(primary_key=True)
    activity_id = models.IntegerField(blank=True, null=True)
    organization_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'collaborator'


class CollaboratorRole(models.Model):
    role_on_event = models.CharField(primary_key=True, max_length=50)
    colab_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'collaborator_role'


class Documentation(models.Model):
    documentation_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(blank=True, null=True)
    event_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'documentation'


class DocumentationDesc(models.Model):
    name = models.CharField(primary_key=True, max_length=50)
    documentation_id = models.IntegerField()
    type = models.CharField(max_length=50, blank=True, null=True)
    date_uploaded = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'documentation_desc'


class Organization(models.Model):
    organization_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    fax = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'organization'


class OrganizationEmail(models.Model):
    email = models.CharField(primary_key=True, max_length=50)
    organization_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'organization_email'


class OrganizationTelNo(models.Model):
    tel_no = models.CharField(primary_key=True, max_length=30)
    organization_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'organization_tel_no'


class Permission(models.Model):
    permission_id = models.IntegerField(primary_key=True)
    role_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permission'


class PermissionType(models.Model):
    permission_type = models.CharField(primary_key=True, max_length=100)
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'permission_type'


class Pillar(models.Model):
    pillar_id = models.IntegerField(primary_key=True)
    organization_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pillar'


class PillarDesc(models.Model):
    name = models.CharField(primary_key=True, max_length=100)
    pillar_id = models.IntegerField()
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pillar_desc'


class Program(models.Model):
    program_id = models.IntegerField(primary_key=True)
    pillar_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'program'


class ProgramDesc(models.Model):
    name = models.CharField(primary_key=True, max_length=50)
    program_id = models.IntegerField()
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'program_desc'


class Role(models.Model):
    role_id = models.IntegerField(primary_key=True)
    role_name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'role'


class Staff(models.Model):
    staff_id = models.IntegerField(primary_key=True)
    organization_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staff'


class StaffEmail(models.Model):
    email = models.CharField(primary_key=True, max_length=100)
    staff_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'staff_email'


class StaffInfo(models.Model):
    name = models.CharField(primary_key=True, max_length=100)
    staff_id = models.IntegerField()
    title = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staff_info'


class StaffTelNo(models.Model):
    tel_no = models.CharField(primary_key=True, max_length=100)
    staff_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'staff_tel_no'


class UserPassword(models.Model):
    password = models.CharField(primary_key=True, max_length=255)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_password'


class Users(models.Model):
    user_id = models.IntegerField(primary_key=True)
    staff_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users'


class Venue(models.Model):
    venue_id = models.IntegerField(primary_key=True)
    activity_id = models.IntegerField(blank=True, null=True)
    start_date = models.CharField(max_length=100, blank=True, null=True)
    end_date = models.CharField(max_length=100, blank=True, null=True)
    start_time = models.CharField(max_length=100, blank=True, null=True)
    end_time = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'venue'


class VenueDesc(models.Model):
    name = models.CharField(primary_key=True, max_length=100)
    venue_id = models.IntegerField()
    location = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'venue_desc'