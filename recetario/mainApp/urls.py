from django.conf.urls import url, include
from mainApp.views import *

urlpatterns = [
    url("/test", inicio)
]