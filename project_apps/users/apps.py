from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'project_apps.users'  # Nombre completo de la app

    def ready(self):
        import project_apps.users.signals
