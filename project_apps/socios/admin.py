from django.contrib import admin
from .models import Socio, DocumentoSocio


@admin.register(Socio)
class SocioAdmin(admin.ModelAdmin):
    list_display = ('numero_padron', 'nombre', 'apellido', 'dni', 'placa', 'telefono')
    search_fields = ('numero_padron', 'dni', 'nombre', 'apellido')
    list_filter = ('placa',)


@admin.register(DocumentoSocio)
class DocumentoSocioAdmin(admin.ModelAdmin):
    list_display = ('socio', 'tipo_documento', 'fecha_subida')
    search_fields = ('socio__username', 'tipo_documento')
    list_filter = ('tipo_documento', 'fecha_subida')
