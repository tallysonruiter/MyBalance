from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from balanca.models import Pessoa,Peso
from balanca.serializers import PessoaSerializer, PesoSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

   
class PesoDetail(APIView):

    def get_object(self, pk):
        try:
            return Peso.objects.get(pk=pk)
        except Peso.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        peso = self.get_object(pk)
        serializer = PesoSerializer(peso)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        peso = self.get_object(pk)
        peso.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class peso_list(APIView):
  

    def get(self, request, format=None):
        peso = Peso.objects.all()
        serializer = PesoSerializer(peso, many=True)
        return Response(serializer.data)
     
    def post(self, request, format=None):
        serializer = PesoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

    def delete(self, request, pk, format=None):
        peso = self.get_object(pk)
        peso.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

        
    #-----------------------------Pessoa-------------------------------------------# 
      
        
        
class PessoaDetail(APIView):

    def get_object(self, pk):
        try:
            return Pessoa.objects.get(pk=pk)
        except Pessoa.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        pessoa = self.get_object(pk)
        serializer = PessoaSerializer(pessoa)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        pessoa = self.get_object(pk)
        pessoa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class pessoa_list(APIView):
  

    def get(self, request, format=None):
        pessoa = Pessoa.objects.all()
        serializer = PessoaSerializer(pessoa, many=True)
        return Response(serializer.data)
     
    def post(self, request, format=None):
        serializer = PessoaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

    def delete(self, request, pk, format=None):
        pessoa = self.get_object(pk)
        pessoa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
