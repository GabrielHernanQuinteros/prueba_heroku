"""Universidad URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from Aplicaciones.Academico.views import *
from Aplicaciones.core.views import *

#========================================================================================
# con el INCLUDE indicamos en que otros URLS.PY podra buscar la pagina solicitada, el primer parametro indica
# una cadena inicial de busqueda, que se suma al nombre de la url. 
# path('xxx', include('Aplicaciones.Academico.urls'))
# path('xxx/', include('Aplicaciones.Academico.urls'))

from django.urls import path, include

from django.conf import settings     # Agregado para Heroku
from django.conf.urls.static import static     # Agregado para Heroku


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Aplicaciones.Academico.urls')),
    path('', include('Aplicaciones.core.urls'))
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)     # Agregado para Heroku


#========================================================================================
# Si esta en modo DEBUG que podamos acceder a las imagenes guardadas en nuestro disco local
#
#if settings.DEBUG:
#    from django.conf.urls.static import static
#    urlpatterns += static(settings.MEDIA_URL, 
#        document_root=settings.MEDIA_ROOT)
#========================================================================================