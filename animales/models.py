from django.db import models


class Animal(models.Model):
    nombre = models.CharField(max_length=35, default='')
    edad = models.IntegerField(default=0)
    especie = models.CharField(default='', max_length=20)

    class Meta:
        verbose_name = 'Animal'
        verbose_name_plural = 'Animales'

    def __str__(self):
        return self.nombre
