from django.shortcuts import render
from .models import *
def WorkPageView(request):
    return render(request,'work.html')

