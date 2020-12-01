# Generated by Django 3.1.3 on 2020-12-01 08:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('roles', models.PositiveSmallIntegerField(blank=True, choices=[(3, 'Pillar Head'), (4, 'Normal User'), (2, 'Management user'), (1, 'Admin')], default=4, null=True)),
                ('email', models.EmailField(max_length=40, unique=True, verbose_name='Email Address')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='Last Name')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': '1 User Register',
            },
        ),
        migrations.CreateModel(
            name='Pillar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Enter pillar Name')),
                ('pillar_desc', models.TextField(blank=True, max_length=500)),
                ('user_pillar', models.ManyToManyField(related_name='pillar', to=settings.AUTH_USER_MODEL, verbose_name='Add Members')),
            ],
            options={
                'verbose_name_plural': '2 Pillar Register',
            },
        ),
    ]
