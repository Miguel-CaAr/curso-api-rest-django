# Generated by Django 5.0.6 on 2024-05-29 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tarea',
            old_name='estadp',
            new_name='estado',
        ),
    ]
