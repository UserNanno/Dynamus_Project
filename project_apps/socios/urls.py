from django.urls import path
from .views import (
    ListaSociosView,
    CrearSocioView,
    SubirDocumentoView,
    MisDocumentosView,
    SocioDashboardView,
    EliminarDocumentoView,
    EditarDocumentoView,
)

urlpatterns = [
    # Dashboard exclusivo para socios autenticados
    path('', SocioDashboardView.as_view(), name='dashboard_socio'),
    
    # Vista exclusiva para administradores
    path('lista-socios/', ListaSociosView.as_view(), name='lista_socios'),
    path('crear-socio/', CrearSocioView.as_view(), name='crear_socio'),  # Nueva ruta para crear socios
    
    # Vistas relacionadas con documentos para socios
    path('subir/', SubirDocumentoView.as_view(), name='subir_documento'),
    path('mis-documentos/', MisDocumentosView.as_view(), name='mis_documentos'),
    path('eliminar/<int:pk>/', EliminarDocumentoView.as_view(), name='eliminar_documento'),
    path('editar/<int:pk>/', EditarDocumentoView.as_view(), name='editar_documento'),
]
