from django.db import models


class Socio(models.Model):
    numero_padron = models.CharField(
        max_length=50, unique=True, verbose_name="Número de padrón"
    )
    dni = models.CharField(
        max_length=8, unique=True, verbose_name="DNI"
    )
    nombre = models.CharField(
        max_length=100, verbose_name="Nombre"
    )
    apellido = models.CharField(
        max_length=100, verbose_name="Apellido"
    )
    placa = models.CharField(
        max_length=50, unique=True, verbose_name="Placa"
    )
    telefono = models.CharField(
        max_length=15, verbose_name="Teléfono"
    )
    direccion = models.TextField(
        verbose_name="Dirección"
    )

    class Meta:
        verbose_name = "Socio"
        verbose_name_plural = "Socios"
        ordering = ['numero_padron']

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.numero_padron})"


class DocumentoSocio(models.Model):
    TIPOS_DOCUMENTO = [
        ('DNI', 'DNI'),
        ('LIC', 'Licencia'),
        ('TAR', 'Tarjeta de Propiedad'),
        ('OTR', 'Otros'),
    ]
    socio = models.ForeignKey(
        Socio, on_delete=models.CASCADE, verbose_name="Socio"
    )
    tipo_documento = models.CharField(
        max_length=3, choices=TIPOS_DOCUMENTO, verbose_name="Tipo de Documento"
    )
    archivo = models.FileField(
        upload_to='documentos_socios/', verbose_name="Archivo"
    )
    fecha_subida = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de Subida"
    )

    class Meta:
        verbose_name = "Documento de Socio"
        verbose_name_plural = "Documentos de Socios"
        ordering = ['-fecha_subida']

    def __str__(self):
        return f"{self.socio.nombre} {self.socio.apellido} - {self.get_tipo_documento_display()}"
