# Generated by Django 4.1.4 on 2023-08-28 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smiledesign_home', '0002_alter_blog_slug_alter_doctors_slug_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='doctors',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='services',
            name='slug',
        ),
    ]
