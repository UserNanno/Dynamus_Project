from django.views.generic import ListView, CreateView
from django.views.generic.edit import DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect
from .models import Socio, DocumentoSocio
from django.contrib.auth.models import User, Group  # Importa Group para roles

class ListaSociosView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    """Vista para administradores: lista de socios."""
    model = Socio
    template_name = 'socios/lista_socios.html'
    context_object_name = 'socios'

    def test_func(self):
        return self.request.user.is_admin()  # Solo administradores pueden acceder

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            return redirect('dashboard_socio')  # Redirige al dashboard del socio si no es admin
        return redirect('login')  # Redirige al login si no está autenticado


# Vista para crear un nuevo socio
from django.contrib.auth import get_user_model  # Importa la función para obtener el modelo de usuario
from django.contrib.auth.models import Group  # Importa Group para roles

class CrearSocioView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Socio
    template_name = 'socios/crear_socio.html'
    fields = ['numero_padron', 'dni', 'nombre', 'apellido', 'placa', 'telefono', 'direccion']
    success_url = reverse_lazy('lista_socios')

    def test_func(self):
        return self.request.user.is_admin()

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            return redirect('dashboard_socio')
        return redirect('login')

    def form_valid(self, form):
        # Guarda primero el socio
        socio = form.save()

        # Obtén el modelo de usuario personalizado
        CustomUser = get_user_model()

        # Crea automáticamente un usuario asociado
        username = socio.dni
        password = socio.dni  # La contraseña por defecto será igual al DNI
        user = CustomUser.objects.create_user(
            username=username,
            password=password,
            first_name=socio.nombre,
            last_name=socio.apellido
        )

        # Asignar al usuario recién creado el rol de "Socio"
        try:
            grupo = Group.objects.get(name='Socio')  # Asegúrate de que el grupo "Socio" exista
            user.groups.add(grupo)
        except Group.DoesNotExist:
            raise ValueError('El grupo "Socio" no existe. Crea este grupo en el administrador de Django.')

        user.save()

        return super().form_valid(form)



class SocioDashboardView(LoginRequiredMixin, ListView):
    """Vista del Dashboard para Socios."""
    model = DocumentoSocio
    template_name = 'socios/dashboard_socio.html'
    context_object_name = 'documentos'
    paginate_by = 10

    def get_queryset(self):
        socio = get_object_or_404(Socio, dni=self.request.user.username)
        queryset = DocumentoSocio.objects.filter(socio=socio)

        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(tipo_documento__icontains=search_query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        socio = get_object_or_404(Socio, dni=self.request.user.username)
        context['socio_nombre'] = f"{socio.nombre} {socio.apellido}"
        return context

class SubirDocumentoView(LoginRequiredMixin, CreateView):
    model = DocumentoSocio
    template_name = 'socios/subir_documento.html'
    fields = ['tipo_documento', 'archivo']
    success_url = reverse_lazy('dashboard_socio')

    def form_valid(self, form):
        socio = get_object_or_404(Socio, dni=self.request.user.username)
        form.instance.socio = socio
        return super().form_valid(form)

class MisDocumentosView(LoginRequiredMixin, ListView):
    model = DocumentoSocio
    template_name = 'socios/mis_documentos.html'
    context_object_name = 'documentos'
    paginate_by = 10

    def get_queryset(self):
        socio = get_object_or_404(Socio, dni=self.request.user.username)
        return DocumentoSocio.objects.filter(socio=socio)

class EliminarDocumentoView(LoginRequiredMixin, DeleteView):
    """Vista para eliminar un documento."""
    model = DocumentoSocio
    template_name = 'socios/eliminar_documento.html'
    success_url = reverse_lazy('mis_documentos')

    def get_queryset(self):
        # Asegúrate de que el usuario solo pueda eliminar sus propios documentos
        socio = get_object_or_404(Socio, dni=self.request.user.username)
        return self.model.objects.filter(socio=socio)

class EditarDocumentoView(LoginRequiredMixin, UpdateView):
    """Vista para reemplazar un documento."""
    model = DocumentoSocio
    template_name = 'socios/editar_documento.html'
    fields = ['tipo_documento', 'archivo']
    success_url = reverse_lazy('mis_documentos')

    def get_queryset(self):
        # Asegúrate de que el usuario solo pueda editar sus propios documentos
        socio = get_object_or_404(Socio, dni=self.request.user.username)
        return self.model.objects.filter(socio=socio)