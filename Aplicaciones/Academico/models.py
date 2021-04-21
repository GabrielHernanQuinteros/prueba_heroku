from django.db import models
from django.utils.html import format_html

from django.contrib.auth.models import User

#========================================================================================
# El primer parametro puede ser un nombre 'legible' para humanos 
# nomb_emp = models.CharField('Empresa', max_length=30, null=True, blank=True)
# DateTimeField()  DateTimeField(auto_now_add=True) DateTimeField(auto_now=True)
# CharField(max_length=30)
# PositiveSmallIntegerField()
# IntegerField(default=0)
# ImageField(upload_to="NombreApp")
# ForeignKey(LaOtraTabla, on_delete=models.CASCADE)
# OneToOneField(LaOtraTabla, on_delete=models.CASCADE, primary_key=True,)

#========================================================================================

class Curso(models.Model):
    nombre = models.CharField(max_length=30)
    creditos = models.PositiveSmallIntegerField()

    # Sobrecarga que indica como se visualizara el registro en el Admin
    def __str__(self):
        auxTexto = "{0} ({1})"
        return auxTexto.format(self.nombre, self.creditos)

    #Sobrecarga que nos deja poner nombres en español o nmotecnicos en el Admin
    class Meta:
        verbose_name = "curso"
        verbose_name_plural = "cursos"
        ordering = ["-creditos"] 

    #========================================================================================
    #def coloreado(self):
    #    if self.creditos >= 4:
    #        return format_html('<span style="color: black;">{0}</span>'.format(self.nombre))
    #    else:
    #        return format_html('<span style="color: red;">{0}</span>'.format(self.nombre))
            
#========================================================================================

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    sistema = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
            
#========================================================================================

class PerfilUsuario(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        )

    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.CASCADE)

    direccion = models.CharField(max_length=200, null=True, blank=True)
    telefono = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.user.username+' - '+self.user.first_name+' '+self.user.last_name
    
    