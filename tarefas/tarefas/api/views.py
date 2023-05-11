from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Tarefa
from api.serializers import TarefaSerializer
from rest_framework import status
from django.http import Http404
# Create your views here.


class ListCreateTarefa(APIView):

    def get(self, request):
        serializer = TarefaSerializer(Tarefa.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TarefaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



...

class DetailUpdateDeleteTarefa(APIView):

    def get_tarefa(self, pk):
        try:
            return Tarefa.objects.get(pk=pk)
        except Tarefa.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        tarefa = self.get_tarefa(pk=pk)
        serializer = TarefaSerializer(tarefa)
        return Response(serializer.data)

    '''def put(self, request, pk):
        tarefa = self.get_tarefa(pk)
        serializer = TarefaSerializer(tarefa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)'''
    


    def delete(self, request, pk):
        tarefa = self.get_tarefa(pk)
        tarefa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, pk):
        tarefa = self.get_tarefa(pk)
        if tarefa.situacao == 'NOVA':
            request.data['situacao'] = tarefa.situacao = 'EM ANDAMENTO'
            tarefa.save()
            serializer = TarefaSerializer(tarefa)
            return Response(serializer.data)
        if tarefa.situacao == 'EM ANDAMENTO':
            request.data['situacao'] = tarefa.situacao = 'RESOLVIDA'
            tarefa.save()
            serializer = TarefaSerializer(tarefa)
            return Response(serializer.data)