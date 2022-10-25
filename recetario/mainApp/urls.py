from django.urls import path
from django.urls.resolvers import URLPattern
from mainApp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", inicio),
    path("add/", addReceta),
    path("receta/<int:id>/", verReceta, name="receta")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
