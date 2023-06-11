from django.shortcuts import render
from .models import AboutMe

def home(request):
    about = AboutMe.objects.all().first()

    context = {
        "about":about
    }
    print(about.resume)
    return render(request,'home.html',context)
