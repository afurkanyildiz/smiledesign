from django.shortcuts import render
from .models import Blog,Doctors,Services
from django.http import Http404
from django.shortcuts import get_object_or_404


def base_view(request):
    services = Services.objects.all()
    context = {'services': services}
    return context


def home_page(request):
    context =base_view(request)
    return render(request,'smiledesign_home/home.html',context)


def about_page(request):
    context =base_view(request)
    return render(request,'smiledesign_home/about.html',context)

def services_page(request):
    services = Services.objects.filter(is_active=True)
    numbers = list(range(1, services.count()))
    context = base_view(request)
    context['services'] = services
    context['numbers'] = numbers
    # context = dict(services=services,numbers=numbers)
    return render(request,'smiledesign_home/services.html',context)

def doctors_page(request):
    doctors = Doctors.objects.filter(is_active=True)
    context = base_view(request)
    context['doctors'] = doctors
    # context = dict(doctors=doctors)
    return render(request,'smiledesign_home/doctors.html',context)

def blog_page(request):
    blogs = Blog.objects.filter(is_active=True)
    context = base_view(request)
    context['blogs'] = blogs
    # context = dict(blogs = blogs)
    return render(request,'smiledesign_home/blog.html',context)

def contact_page(request):
    context = base_view(request)
    return render(request,'smiledesign_home/contact.html',context)

def blog_detail_page(request, id ): 
    blog = get_object_or_404(Blog, pk=id)
    context = base_view(request)
    context['blog'] = blog
    # context = dict(blog=blog)
    return render(request,'smiledesign_home/details/blog_details.html',context)

def services_detail_page(request, id ): 
    # services = Services.objects.get(pk=id)
    # context = base_view(request)
    # context['services'] = services
    # # print(services.services_description)
    # # context = dict(services=services)
    # return render(request,'smiledesign_home/details/services_details.html',context) 
    services_object = get_object_or_404(Services, pk=id)
    services = Services.objects.all()  # Menü verilerini al
    context = {'services_object': services_object, 'services': services}
    return render(request, 'smiledesign_home/details/services_details.html', context)




