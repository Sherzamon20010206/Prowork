from django.shortcuts import render
from .models import Kitob
# Create your views here.
import json
from django.http import JsonResponse, HttpResponse
def KitoblarPageView(request):
    books=Kitob.objects.all().order_by("data")[::-1]

    context={
        'books':books,
    }
    return render(request,'books.html',context)

def Search(request):
    books = Kitob.objects.all().order_by("data")[::-1]


    if request.method=="POST":
        data = json.loads(request.body)
        print(data)
        print(data['search'])

        if data['search']=="pustoy":
            data_book = []
            for book in books:
                context = {
                    'title': book.title,
                    'type': book.type.type,
                    'img': book.img.url,
                    'file': book.file.url,

                }
                data_book.append(context)

            return JsonResponse({'data':data_book})
        else:

            search=data['search']

            books = Kitob.objects.filter(tag__contains=search)
            for i in books:
                print("qidiruv: ",i)
            data_book = []
            for book in books:
                context = {
                    'title': book.title,
                    'type': book.type.type,
                    'img': book.img.url,
                    'file': book.file.url,

                }
                data_book.append(context)

            return JsonResponse({'data':data_book})








