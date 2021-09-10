from rest_framework import viewsets
from livros.api import serializers
from livros import models

class LivroViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.LivroSerializer
    queryset = models.Livro.objects.all()