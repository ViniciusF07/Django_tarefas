from django.urls import path
from .views import (ListCreateTarefa, DetailUpdateDeleteTarefa)
urlpatterns = [
    # API Filmes
    path('tarefas', ListCreateTarefa.as_view(), name='list-create-tarefa'),
    path('tarefas/<int:pk>', DetailUpdateDeleteTarefa.as_view(),
         name='detail-update-delete-tarefa')
    
]
