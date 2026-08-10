from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("tiendalibre.urls")),
    path("home/", include("tiendalibre.urls")),
    path("productos/", include("tiendalibre.urls")),
    path("acerca_de_mi/", include("tiendalibre.urls"))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
