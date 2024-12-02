from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from project_apps.socios.models import Socio, DocumentoSocio

User = get_user_model()

def run():
    # Datos del nuevo usuario administrador
    username = "root"
    email = "root@gmail.com"
    password = "root"
    first_name = "Admin"
    last_name = "Socio"
    role = "ADMIN"  # Rol del usuario (Administrador)

    # Crear el grupo "Socio" si no existe
    group_name = "Socio"
    group, created = Group.objects.get_or_create(name=group_name)
    if created:
        print(f"Grupo '{group_name}' creado.")

    # Asignar permisos al grupo "Socio"
    permissions = []
    for model in [Socio, DocumentoSocio, User]:
        content_type = ContentType.objects.get_for_model(model)
        perms = Permission.objects.filter(content_type=content_type)
        permissions.extend(perms)

    group.permissions.set(permissions)
    group.save()
    print(f"Permisos asignados al grupo '{group_name}'.")

    # Crear el usuario si no existe
    if not User.objects.filter(username=username).exists():
        print(f"Creando usuario administrador ({username})...")
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            role=role,
        )
        user.groups.add(group)  # Asignar el grupo "Socio"
        user.is_staff = True  # Permitir acceso al panel de administración
        user.is_active = True
        user.save()
        print(f"Usuario administrador '{username}' creado con éxito.")
    else:
        print(f"El usuario '{username}' ya existe.")
