from django.urls import path

# Importa todas las vistas de esta APP
from Aplicaciones.Academico.views import *


#========================================================================================
# En el ejemplo vemos como indicamos que recibira un parametro del usuario en el navegador
# 
# ej: /polls/5/        path('<int:question_id>/', views.detail, name='detail')
# 
# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)
#========================================================================================


urlpatterns = [
    path('vistasimple/', vwVistaSinTemplate),
    path('listado/', vwListadoBasico, name="ListadoBasico"),
    path('listadoclases/', vwListadoClases.as_view(), name="ListadoDeClases"),
    path('Curso/<int:parIdCurso>', vwConsultaPorId, name="ConsultaPorId")
]

