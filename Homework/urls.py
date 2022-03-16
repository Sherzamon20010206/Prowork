from django.contrib import admin
from django.urls import re_path as url
from django.urls import path,include
from django.views.static import serve
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),

    path('',include("homepage.urls"),name='homepage'),
    path('work/',include("workpage.urls")),
    path('kirish/',include("login.urls")),
    path('kitoblar/',include("kitoblar.urls")),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
