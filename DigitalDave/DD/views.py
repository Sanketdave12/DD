from django.shortcuts import HttpResponse, render, redirect
from .models import *
from django.contrib import messages

def home(request):
    return render(request, 'index.html')

def contactUs(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        website = request.POST['website']
        if len(email) < 3 or len(phone) < 10 or len(message) < 4:
            messages.error(request, 'Please fill the form correctly.')
        else:
            messages.success(
                request, 'Your message has been successfully sent.')
        contact = Contact(name=name, email=email,
                          phone_no=phone, message=message, website=website)
        contact.save()
        return redirect('/')
    return render(request, './index.html')
