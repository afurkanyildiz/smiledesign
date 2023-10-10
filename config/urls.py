"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from smiledesign_home.views import home_page,about_page,services_page,doctors_page, blog_page,contact_page,blog_detail_page,services_detail_page,doctor_details_page,contact_form_view


urlpatterns = [
    # path('base', base_view, name='base_view'),
    path('', home_page, name='home_page'),
    path('about/', about_page,name='about_page'),
    path('services/', services_page,name='services_page'),
    path('doctors/', doctors_page, name='doctors_page'),
    path('blog/', blog_page, name='blog_page'),
    path('contact/', contact_page, name='contact_page'),
    path('blog/<int:id>/', blog_detail_page, name='blog_detail_page'),
    path('services/<int:id>/', services_detail_page, name='services_detail_page'),
    path('doctor/<int:id>/', doctor_details_page, name='doctor_details_page'),
    path('contact_form_submit/', contact_form_view, name='contact_form_view'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
