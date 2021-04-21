from django.contrib import admin

# Importamos los modelos agregados para enriquecer la tabla de USUARIOS
from .models import Categoria, PerfilUsuario

# Importamos cada uno de los modelos que necesitamos agregar de esta Aplicacion
from .models import Curso

#========================================================================================

# Agregado basico para que incluya la tabla Curso en el Admin
admin.site.register(Curso)
admin.site.register(Categoria)
admin.site.register(PerfilUsuario)

#========================================================================================
# Ejemplo para poner campos de READ ONLY en el Admin
#
#class ProjectAdmin(admin.ModelAdmin):
#    readonly_fields = ('created', 'updated')
#
#admin.site.register(Project, ProjectAdmin)
#========================================================================================


#========================================================================================
# Ejemplos de personalizacion para el Admin
#
#class CursoAdmin(admin.ModelAdmin):
#    list_display = ('id', 'curso', 'creditos')
    # ordering = ('creditos', 'nombre')
    # search_fields = ('nombre', 'creditos')
    # list_editable = ('nombre','creditos')
    # list_display_links = ('nombre',)
    # list_filter = ('creditos',)
    # list_per_page = 3 # Paginación
    # exclude = ('creditos',)

#    """
#    fieldsets = (
#        (None, {
#            'fields': ('nombre',)
#        }),
#        ('Advanced options', {
#            'classes': ('collapse', 'wide', 'extrapretty'),
#            'fields': ('creditos',)
#        })
#    )
#    """

#    def datos(self, obj):
#        return obj.nombre.upper()

#    datos.short_description = "CURSO (MAYÚS)"
#    datos.empty_value_display = "???"
#    datos.admin_order_field = 'nombre'




#admin.site.register(Curso, CursoAdmin)
