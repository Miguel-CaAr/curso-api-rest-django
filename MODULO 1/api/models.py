from django.db import models


class Curso(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=250)
    imagen = models.CharField(max_length=250)

    def __str__(self):
        return self.titulo
