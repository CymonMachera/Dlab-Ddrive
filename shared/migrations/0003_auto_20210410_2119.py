# Generated by Django 3.1.6 on 2021-04-10 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0002_auto_20210407_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='sharedfolder',
            name='activity_id',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='sharedfolder',
            name='pillar_id',
            field=models.CharField(default=None, max_length=2),
        ),
        migrations.AddField(
            model_name='sharedfolder',
            name='program_id',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='sharedfile',
            name='file_link',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='sharedfolder',
            name='folder_link',
            field=models.CharField(default=None, max_length=100),
        ),
    ]