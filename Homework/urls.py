from django.contrib import admin

from django.urls import path,include

from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),

    path('',include("homepage.urls"),name='homepage'),
    path('work/',include("workpage.urls")),
    path('kirish/',include("login.urls")),
    path('kitoblar/',include("kitoblar.urls")),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)