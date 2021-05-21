# Generated by Django 3.1.6 on 2021-04-07 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sharedfile',
            name='file_id',
        ),
        migrations.RemoveField(
            model_name='sharedfolder',
            name='folder_id',
        ),
        migrations.AddField(
            model_name='sharedfile',
            name='file_link',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='sharedfolder',
            name='folder_link',
            field=models.CharField(default=None, max_length=50),
        ),
    ]