# Generated by Django 4.1.4 on 2023-10-05 08:40

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smiledesign_home', '0004_blog_thumbnail_large_blog_thumbnail_medium_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
