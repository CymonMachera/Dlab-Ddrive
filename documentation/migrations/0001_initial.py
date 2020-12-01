# Generated by Django 3.1.3 on 2020-12-01 08:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('program', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Uploads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_name', models.CharField(max_length=50)),
                ('doc_type', models.PositiveSmallIntegerField(blank=True, choices=[(3, 'Images'), (2, 'Video'), (1, 'Documents')])),
                ('dete_uploaded', models.DateTimeField(auto_now_add=True)),
                ('upload_path', models.FileField(upload_to='pillar', verbose_name='Choose File')),
                ('activity_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='program.activity')),
                ('uploader_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Documentations',
            },
        ),
    ]
