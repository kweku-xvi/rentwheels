# Generated by Django 4.2.1 on 2024-10-17 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='transmission_choices',
            new_name='transmission',
        ),
    ]
