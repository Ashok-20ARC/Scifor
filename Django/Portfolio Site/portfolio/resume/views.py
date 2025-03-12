from django.shortcuts import render
from .models import Profile,Experience,Project

# Create your views here.
def home(request):
    profile=Profile.objects.first()
    experiences=Experience.objects.all()
    projects=Project.objects.all()
    return render(request,'resume/home.html',{
        'profile':profile,
        'experiences':experiences,
        'projects':projects
    })
