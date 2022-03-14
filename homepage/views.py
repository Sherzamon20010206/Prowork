from django.shortcuts import render
from.models import *
# Create your views here.
def HomePageView(request):
    return render(request,'index.html')