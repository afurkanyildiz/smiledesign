from django.contrib import admin
from .models import Blog,Doctors


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


# Register your models here.
