import livros
from django.contrib import admin
from django.contrib.admin.filters import SimpleListFilter

from .models import Livro
# Register your models here.

class FiltroGenero(SimpleListFilter):
    title = "Gêneros mais lidos"
    parameter_name = "Gêneros mais lidos"
    def lookups(self, request, model_admin):
        return (
            ("fantasia", "Fantasia"),
            ("romance", "Romance"),
            ("terror", "Terror"),
        )
    def queryset(self, request, queryset):
        if self.value() == "fantasia":
            queryset = queryset.filter(genero__contains = "fantasia")
        elif self.value() == "romance":
            queryset = queryset.filter(genero__contains = "romance")
        elif self.value() == "terror":
            queryset = queryset.filter(genero__contains = "terror")
        return queryset

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "genero", "qtd_paginas")
    list_filter = ["autor", FiltroGenero]