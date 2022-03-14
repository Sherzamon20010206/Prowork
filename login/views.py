from django.shortcuts import render

# Create your views here.
def LoginPageView(request):
    return  render(request,"login.html")