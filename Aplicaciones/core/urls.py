from django.urls import path

from Aplicaciones.core.views import *



urlpatterns = [
    path('', home, name="home")
]
