from django.shortcuts import render

# Create your views here.
def KitoblarPageView(requests):
    return render(requests,'books.html')