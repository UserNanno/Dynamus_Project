from django.contrib import admin
from django.urls import path, include
from project_apps.users.views import CustomLoginView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # Administración
    path('users/', include('project_apps.users.urls')),  # Rutas de usuarios
    path('socios/', include('project_apps.socios.urls')),  # Rutas de socios
    path('login/', CustomLoginView.as_view(), name='login'),  # Login
    path('', CustomLoginView.as_view(), name='home'),  # Login por defecto si no autenticado
]


# Solo para desarrollo, sirve los archivos media
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)