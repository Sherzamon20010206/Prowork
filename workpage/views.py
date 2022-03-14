from django.shortcuts import render
from .models import *
def WorkPageView(request):
    documents=Document.objects.all()
    sorts=Sort.objects.all()

    context={
        "works":documents,
        "sorts":sorts,


    }

    return render(request,'work.html',context)

