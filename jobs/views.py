from django.shortcuts import render

# Create your views here.
from .models import Jobs

def Home(request):

    jobs=Jobs.objects
    return render(request,'jobs/home.html',{'jobs':jobs})