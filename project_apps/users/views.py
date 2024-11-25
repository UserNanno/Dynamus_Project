from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages

# Vista personalizada de inicio de sesión
class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True  # Evita mostrar el login si ya está autenticado

    def get_success_url(self):
        user = self.request.user
        if user.is_admin():
            return reverse_lazy('lista_socios')  # Redirige a la vista de lista de socios
        elif user.is_socio():
            return reverse_lazy('dashboard_socio')  # Redirige al dashboard del socio
        return reverse_lazy('home')  # URL de fallback (por defecto)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.get_success_url())  # Redirige si ya está autenticado
        return super().dispatch(request, *args, **kwargs)


# Vista personalizada de cierre de sesión
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        request.session.flush()
        messages.add_message(request, messages.INFO, "Has cerrado sesión exitosamente.")
        return super().dispatch(request, *args, **kwargs)
