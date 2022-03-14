from  django.urls  import path
from .views import *
urlpatterns=[
    path('',LoginPageView,name="login")
]