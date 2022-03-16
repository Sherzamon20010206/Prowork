from  django.urls  import path
from .views import *
urlpatterns=[
    path('',LoginPageView,name="login"),
    path('user_login/',Save,name="save"),
    path('logout/',custom_logout,name="logout"),
]