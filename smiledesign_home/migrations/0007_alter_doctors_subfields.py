# Generated by Django 4.1.4 on 2023-08-21 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smiledesign_home', '0006_doctors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctors',
            name='subfields',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]