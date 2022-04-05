# Generated by Django 3.1.3 on 2022-04-05 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapi', '0003_auto_20220405_1134'),
    ]

    operations = [
        migrations.CreateModel(
            name='SingleTodoList',
            fields=[
                ('todo_id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('Completed', 'Completed'), ('Pending', 'Pending')], max_length=50)),
                ('title', models.TextField(max_length=100)),
                ('description', models.TextField(max_length=250)),
            ],
            options={
                'db_table': 'SingleTodoList',
            },
        ),
    ]