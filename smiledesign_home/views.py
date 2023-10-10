from PIL import Image
from django.shortcuts import render
from .models import Blog,Doctors,Services
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
import os


def base_view(request):
    services = Services.objects.all()
    context = {'services': services}
    return context

#PAGE

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


#DETAILS

def blog_detail_page(request, id ): 
    blog = get_object_or_404(Blog, pk=id)
    context = base_view(request)
    context['blog'] = blog
    return render(request,'smiledesign_home/details/blog_details.html',context)

def services_detail_page(request, id ): 
    services_object = get_object_or_404(Services, pk=id)
    services = Services.objects.all()  # Menü verilerini al
    context = {'services_object': services_object, 'services': services}
    return render(request, 'smiledesign_home/details/services_details.html', context)

def doctor_details_page(request,id):
    doctor = get_object_or_404(Doctors, pk=id)
    context =base_view(request)
    context['doctor'] = doctor
    return render(request,'smiledesign_home/details/blog_details.html',context)

def contact_form_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        telephone = request.POST['telephone']
        email = request.POST['email']
        description = request.POST['description']
        
        subject = f'İletişim Formu - {username}'
        message= f'İsim Soyisim: {username}\n Telefon Numarası: {telephone}\n Email Adresi:{email}\n Mesaj:{description}'
        
        from_email = settings.EMAIL_HOST_USER
        recipient_list = ['afurkanyildizz@gmail.com']
        send_mail(subject,message,from_email,recipient_list)
        print('Gonderildi')
        return render(request,'smiledesign_home/blog.html')
    print('Gonderilmedi')
    return render(request,'smiledesign_home/contact.html')
        


#FUNCTIONS
# @receiver(post_save, sender=Blog)
# def resize_images(sender,instance,**kwargs):
#     if instance.image:
#         # image = Image.open(instance.image.path)

#         # # Boyutları ayarlayın
#         # small_size = (100, 100)
#         # medium_size = (300, 300)
#         # large_size = (600, 600)

#         # Küçük boyutlu resim
#         # image.thumbnail(small_size)
#         # instance.thumbnail_small.save(instance.image.name, image)

#         # # Orta boyutlu resim
#         # image.thumbnail(medium_size)
#         # instance.thumbnail_medium.save(instance.image.name, image)

#         # # Büyük boyutlu resim
#         # image.thumbnail(large_size)
#         # instance.thumbnail_large.save(instance.image.name, image)
        
#         # Küçük boyutlu resim
#         # image = Image.open(instance.image.path) 
#         image = Image.open(instance.image.path)

#         # Boyutları ayarlayın
#         small_size = (100, 100)
#         medium_size = (300, 300)
#         large_size = (600, 600)

#         # Küçük boyutlu resim
#         image.thumbnail(small_size)
#         small_image_path = os.path.join('', instance.image.name.replace('.', '_small.'))
#         image.save(small_image_path)  # Özel dosya yolu ile kaydedin

#         # Orta boyutlu resim
#         image = Image.open(instance.image.path)  # Görüntüyü tekrar açın
#         image.thumbnail(medium_size)
#         medium_image_path = os.path.join('', instance.image.name.replace('.', '_medium.'))
#         image.save(medium_image_path)  # Özel dosya yolu ile kaydedin

#         # Büyük boyutlu resim
#         image = Image.open(instance.image.path)  # Görüntüyü tekrar açın
#         image.thumbnail(large_size)
#         large_image_path = os.path.join('', instance.image.name.replace('.', '_large.'))
#         image.save(large_image_path) 