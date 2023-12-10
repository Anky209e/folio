from django.shortcuts import render
from .models import AboutMe,Skill

def home(request):
    about = AboutMe.objects.all().first()

    context = {
        "about":about
    }
    print(about.resume)
    return render(request,'home.html',context)

def about(request):
    about = AboutMe.objects.all().first()
    skill = Skill.objects.all()
    print(skill)
    context = {
        "about":about,
        "skills":skill
    }

    return render(request,'about.html',context)

def contact(request):
    return render(request,'contact.html')