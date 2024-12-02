from django.contrib.auth import get_user_model

User = get_user_model()

def run():
    username = "root"
    email = "root@gmail.com"
    password = "root"

    if not User.objects.filter(username=username).exists():
        print(f"Creando superusuario ({username})...")
        User.objects.create_superuser(username=username, email=email, password=password)
        print("Superusuario creado.")
    else:
        print("Superusuario ya existe.")
