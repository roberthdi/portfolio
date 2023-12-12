from django.db import models

# Create your models here.
class Certificados(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="titulo")
    habilidades = models.TextField(verbose_name="habilidades")
    image = models.ImageField(verbose_name="image", upload_to="media")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Edicion" )

    def __str__(self):
        return self.titulo