from  django.urls  import path
from .views import *
urlpatterns=[
    path('',KitoblarPageView,name="book")
]