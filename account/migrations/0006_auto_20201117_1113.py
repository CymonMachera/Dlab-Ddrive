# Generated by Django 3.1.3 on 2020-11-17 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20201117_1106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='roles',
        ),
        migrations.AddField(
            model_name='customuser',
            name='roles',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'pillar_head'), (2, 'normal-user'), (3, 'management_user')], default=7, null=True),
        ),
        migrations.DeleteModel(
            name='Role',
        ),
    ]
