from django.db import models

# Create your models here.
class Tarefa(models.Model):
    descricao = models.CharField()
    responsavel = models.CharField()
    nivel = models.PositiveIntegerField()
    prioridade = models.PositiveIntegerField()
    situacao = models.CharField()