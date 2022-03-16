from django.shortcuts import render
from .models import *
import json
from django.db.models import Q

from django.http import JsonResponse, HttpResponse
def WorkPageView(request):
    documents=Document.objects.all().order_by("data")[::-1]
    sorts=Sort.objects.all()

    context={
        "works":documents,
        "sorts":sorts,


    }

    return render(request,'work.html',context)

def Search(request):
    files = Document.objects.all().order_by("data")[::-1]


    if request.method=="POST":
        data = json.loads(request.body)
        print(data)

        print(data['search'])

        if data['search']=="pustoy":
            data_file = []
            for file in files:
                context = {
                    'title': file.title,

                    'img': file.img.url,
                    'file': file.file.url,

                }
                data_file.append(context)

            return JsonResponse({'data':data_file})
        else:

            search=data['search']

            files = Document.objects.filter(Q(tag__contains=search)|Q(title__contains=search))

            data_file = []
            for file in files:
                context = {
                    'title': file.title,

                    'img': file.img.url,
                    'file': file.file.url,

                }
                data_file.append(context)

            return JsonResponse({'data':data_file})