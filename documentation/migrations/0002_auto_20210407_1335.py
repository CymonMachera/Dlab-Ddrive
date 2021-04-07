# Generated by Django 3.1.6 on 2021-04-07 10:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('documentation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploads',
            name='os_file',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='folder',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
