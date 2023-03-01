from django.db import models

class Categoria(models.Model):
    nome = models.Charfield(max_length=100)
    dc_criacao = models.DateTimeField(auto_now_add=True)

# Crie seus modelos aqui.
