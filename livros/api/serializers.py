from django.db.models import fields
from rest_framework import serializers
from livros import models

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Livro
        fields = '__all__'
