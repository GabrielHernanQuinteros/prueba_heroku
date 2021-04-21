from django.shortcuts import render
from .models import Curso

#========================================================================================
# Importacion para la VISTA SIMPLE SIN TEMPLATE
from django.http import HttpResponse
#========================================================================================
# Importacion para LISTADO USANDO CLASES
from django.views.generic import ListView
#========================================================================================


def vwVistaSinTemplate(request):
    return HttpResponse("Soy una vista sin usar template")

#========================================================================================

def vwListadoBasico(request):

    objCursosListados = Curso.objects.all()

    dccDatos = {
        'parTitulo': 'Listado de Cursos',
        'parCursos': objCursosListados
    }

    return render(request, "ListadoDeCursos.html", dccDatos)

#========================================================================================

class vwListadoClases(ListView):
    model = Curso
    template_name = 'ListadoDeCursosClases.html'

#========================================================================================

def vwConsultaPorId(request, parIdCurso):

    objCursosListados = Curso.objects.filter(id=parIdCurso)

    dccDatos = {
        'parTitulo': 'Consulta Curso Id %s' % parIdCurso,
        'parCursos': objCursosListados
    }

    return render(request, "ConsultaPorId.html", dccDatos)

#========================================================================================