from django.shortcuts import render
from .models import *
from kitoblar import models
from django.views.generic import TemplateView, ListView, DetailView
# Create your views here.
def HomePageView(request):
    books=models.Kitob.objects.all().order_by('data')[:6]

    context={
        'books':books,
    }






    return render(request,'index.html',context)

