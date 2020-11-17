# Generated by Django 3.1.3 on 2020-11-16 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20201113_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='roles',
            field=models.ManyToManyField(choices=[(1, 'pillar_head'), (2, 'normal-user'), (3, 'management_user')], default=2, to='account.Role'),
        ),
    ]
