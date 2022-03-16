from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.shortcuts import render
from .models import *
from django.contrib.auth import authenticate,login
from django.views.generic import TemplateView, ListView, DetailView
import json
from django.http import JsonResponse, HttpResponseRedirect


# Create your views here.


def LoginPageView(request):
    return  render(request,"login.html")
def Save(request):
    if request.method=='POST':
        data=json.loads(request.body)
        print(data)
        name=data['login']
        password = data['password']

        user = authenticate(username=name,password=password)

        if user is not None:
            login(request, user)

            return JsonResponse({'data': 'ok'})


        else:

            return JsonResponse({'data': 'not'})



def custom_logout(request):

    auth.logout(request)

    return HttpResponseRedirect('/')