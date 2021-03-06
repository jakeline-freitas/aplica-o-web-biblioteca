from django.db import models

# Create your models here.
class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=45)
    genero = models.CharField(max_length=45)
    qtd_paginas = models.IntegerField(verbose_name='Número de páginas')

    class Meta:
        ordering = ("titulo",)

    def __str__(self):
        return self.titulo


