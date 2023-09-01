# Generated by Django 4.1.4 on 2023-08-28 09:04

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smiledesign_home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='', editable=True, populate_from='title', unique=True),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='', editable=True, populate_from='doctor_name', unique=True),
        ),
        migrations.AlterField(
            model_name='services',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='', editable=True, populate_from='services_name', unique=True),
        ),
    ]
