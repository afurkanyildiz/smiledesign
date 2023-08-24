from django.shortcuts import render
from .models import Blog,Doctors,Services
from django.http import Http404
from django.shortcuts import get_object_or_404


def home_page(request):
    return render(request,'smiledesign_home/home.html',{})


def about_page(request):
    return render(request,'smiledesign_home/about.html',{})

def services_page(request):
    services = Services.objects.filter(is_active=True)
    numbers = list(range(1, services.count()))

    context = dict(services=services,numbers=numbers)
    return render(request,'smiledesign_home/services.html',context)

def doctors_page(request):
    doctors = Doctors.objects.filter(is_active=True)
    context = dict(doctors=doctors)
    return render(request,'smiledesign_home/doctors.html',context)

def blog_page(request):
    blogs = Blog.objects.filter(is_active=True)
    context = dict(blogs = blogs)
    return render(request,'smiledesign_home/blog.html',context)

def contact_page(request):
    return render(request,'smiledesign_home/contact.html',{})

def blog_detail_page(request, id ): 
    blog = get_object_or_404(Blog, pk=id)
    print(id)
    context = dict(blog=blog)
    return render(request,'smiledesign_home/details/blog_details.html',context)

def services_detail_page(request, id ): 
    services = get_object_or_404(Services, pk=id)
    print(id)
    context = dict(services=services)
    return render(request,'smiledesign_home/details/services_details.html',context)

# Create your views here.
