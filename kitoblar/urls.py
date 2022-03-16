from  django.urls  import path
from .views import *
urlpatterns=[
    path('',KitoblarPageView,name="book"),
    path('search/',Search,name="search"),
]