from django.contrib import admin
from .models import Blog,Doctors,Services
from django.db import models
from ckeditor.widgets import CKEditorWidget

formfield_overrides={models.TextField:{'widget':CKEditorWidget()}}
class BlogAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'is_active',
        # 'created_at',
        # 'updated_at'
    ]

    
admin.site.register(Blog, BlogAdmin)

class DoctorsAdmin(admin.ModelAdmin):
    list_display=[
        'doctor_name',
        'is_active', 
    ]
admin.site.register(Doctors,DoctorsAdmin)

class ServicesAdmin(admin.ModelAdmin):
    list_display=[
        'services_name',
        'is_active', 
    ]
admin.site.register(Services,ServicesAdmin)


# Register your models here.
