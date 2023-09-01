from django.db import models
from django.contrib.auth.models import User
# from django_autoslug import AutoSlugField

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to='blog_images',null=True,blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    # slug = AutoSlugField(populate_from='title', unique=True,default='',editable=True)
    
    def __str__(self):
        return self.title
    
    

class Doctors(models.Model):
    doctor_name = models.CharField(max_length=200)
    field_of_expertise = models.CharField(max_length=1000)
    subfields = models.CharField(max_length=1000,blank=True,null=True)
    doctor_image=models.ImageField(upload_to='doctors_images',null=True,blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # slug = AutoSlugField(populate_from='doctor_name', unique=True,default='',editable=True)
    
    def __str__(self):
        return self.doctor_name


class Services(models.Model):
    services_name = models.CharField(max_length=400)
    services_description = models.TextField()
    services_image = models.ImageField(upload_to='services_images', null=True,blank=True)
    is_active = models.BooleanField(default=True)
    # slug = AutoSlugField(populate_from='services_name', unique=True,default='',editable=True)
    
    
    def __str__(self):
        return self.services_name
    