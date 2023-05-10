from django.urls import path
from .views import Tarefa
urlpatters = [
    path('tarefas/', Tarefa.as_view(), name='hello')
]
