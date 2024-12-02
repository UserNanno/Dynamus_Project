from django.urls import path
from .views import (
    ListaSociosView,
    CrearSocioView,
    SubirDocumentoView,
    MisDocumentosView,
    SocioDashboardView,
    EliminarDocumentoView,
    EditarDocumentoView,
    EditarSocioView,
    EliminarSocioView,
    VerDocumentosView
)

urlpatterns = [
    # Dashboard exclusivo para socios autenticados
    path('', SocioDashboardView.as_view(), name='dashboard_socio'),
    
    # Vista exclusiva para administradores
    path('lista-socios/', ListaSociosView.as_view(), name='lista_socios'),
    path('crear-socio/', CrearSocioView.as_view(), name='crear_socio'),
    
    # Vistas relacionadas con documentos para socios
    path('documentos/subir/', SubirDocumentoView.as_view(), name='subir_documento'),
    path('documentos/mis/', MisDocumentosView.as_view(), name='mis_documentos'),
    path('documentos/eliminar/<int:pk>/', EliminarDocumentoView.as_view(), name='eliminar_documento'),
    path('documentos/editar/<int:pk>/', EditarDocumentoView.as_view(), name='editar_documento'),

    # Vistas relacionadas con socios
    path('socios/editar/<int:pk>/', EditarSocioView.as_view(), name='editar_socio'),
    path('socios/eliminar/<int:pk>/', EliminarSocioView.as_view(), name='eliminar_socio'),
    path('socios/documentos/<int:pk>/', VerDocumentosView.as_view(), name='ver_documentos'),
]

