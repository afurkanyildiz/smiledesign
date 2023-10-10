from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# from django_autoslug import AutoSlugField

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    image = models.ImageField(upload_to='blog_images',null=True,blank=True)
    thumbnail_small = models.ImageField(upload_to='blog_thumbnails/small',blank=True,null=True)
    thumbnail_medium = models.ImageField(upload_to='blog_thumbnails/medium',blank=True,null=True)
    thumbnail_large = models.ImageField(upload_to='blog_thumbnails/large',blank=True,null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    
    def __str__(self):
        return self.title
    
    

class Doctors(models.Model):
    doctor_name = models.CharField(max_length=200)
    field_of_expertise = models.CharField(max_length=1000)
    subfields = models.CharField(max_length=1000,blank=True,null=True)
    doctor_image=models.ImageField(upload_to='doctors_images',null=True,blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.doctor_name


class Services(models.Model):
    services_name = models.CharField(max_length=400)
    services_description = RichTextField()
    services_image = models.ImageField(upload_to='services_images', null=True,blank=True)
    is_active = models.BooleanField(default=True)
    
    
    def __str__(self):
        return self.services_name
    

    