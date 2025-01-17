from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static  # new
from rest_framework import routers

router = routers.DefaultRouter()


urlpatterns = [
    path("", include("game.urls")),
    #path("", include("game.urls_swagger")),
    path("admin/", admin.site.urls),
    path("account", include("django.contrib.auth.urls")),
    path("__debug__/", include("debug_toolbar.urls")),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
