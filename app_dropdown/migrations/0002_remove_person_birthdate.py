# Generated by Django 3.1.2 on 2020-10-24 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_dropdown', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='birthdate',
        ),
    ]
