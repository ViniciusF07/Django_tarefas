
from django.db import models


NIVEL_CHOICES = [
    (1, 1),
    (3, 3),
    (5, 5),
    (8, 8),
]

PRIORIDADE_CHOICES = [
    (1, 1),
    (2, 2),
    (3, 3),
]

SITUACAO_CHOICES = [
    ('NOVA', 'NOVA'),
    ('EM ANDAMENTO', 'EM ANDAMENTO'),
    ('PENDENTE', 'PENDENTE'),
    ('RESOLVIDA', 'RESOLVIDA'),
    ('CANCELADA', 'CANCELADA'),

]


# Create your models here.
class Tarefa(models.Model):
    descricao = models.CharField()
    responsavel = models.CharField()
    nivel = models.PositiveIntegerField(choices=NIVEL_CHOICES)
    prioridade = models.PositiveIntegerField(choices=PRIORIDADE_CHOICES)
    situacao = models.CharField(choices=SITUACAO_CHOICES)