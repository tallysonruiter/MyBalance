from balanca.models import Pessoa,Peso
from rest_framework import serializers

class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = ('nome', 'email', 'datanasc', 'altura', 'peso_inicial', 'sexo','datacadastro','status')

class PesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Peso
        fields = ('id','pessoa', 'peso', 'datapesagem')