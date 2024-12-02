import os

from django.core.wsgi import get_wsgi_application

from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Dynamus.settings')

application = get_wsgi_application()

# Ejecutar migraciones automáticamente en el inicio de la aplicación
try:
    call_command('migrate', interactive=False)
    print("Migraciones aplicadas correctamente.")
except Exception as e:
    print(f"Error al aplicar migraciones: {e}")