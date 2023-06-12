from django.shortcuts import render
from .models import AboutMe

def home(request):
    about = AboutMe.objects.all().first()

    context = {
        "about":about
    }
    print(about.resume)
    return render(request,'home.html',context)

def about(request):
    about = AboutMe.objects.all().first()
    context = {
        "about":about
    }

    return render(request,'about.html',context)

def contact(request):
    return render(request,'contact.html')