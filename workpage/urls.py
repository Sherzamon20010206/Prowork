from  django.urls  import path
from .views import *
urlpatterns=[
    path('',WorkPageView,name="workpage"),
    path('search_file/',Search,name="search"),
]