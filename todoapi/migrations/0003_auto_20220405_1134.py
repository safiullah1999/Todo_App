# Generated by Django 3.1.3 on 2022-04-05 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapi', '0002_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
        migrations.RemoveField(
            model_name='userdetail',
            name='role',
        ),
    ]
