from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Tarefa


class TarefaSerializer(ModelSerializer):
    #usuario = serializers.ReadOnlyField(source='usuario.username')

    class Meta:
        model = Tarefa
        fields = '__all__'