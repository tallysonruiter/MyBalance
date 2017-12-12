from django.db import models

class Pessoa(models.Model):
    MASCULINO = 'M'
    FEMININO = 'F'
    sexo=((MASCULINO, 'Masculino'),(FEMININO, 'Feminino'))
    nome = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    senha = models.CharField(max_length=50)
    datanasc = models.DateField(max_length=50)
    altura = models.CharField(max_length=20)
    peso_inicial = models.CharField(max_length=20)
    sexo = models.CharField(max_length=2,choices=sexo)
    datacadastro = models.DateField(max_length=50)
    status = models.IntegerField(max_length=2)

    def __str__(self):
        return self.nome

class Peso(models.Model):
    #id = models.IntegerField(True)
    pessoa = models.ForeignKey(Pessoa)
    peso = models.CharField(max_length=20)
    datapesagem = models.DateField(max_length=20)
    

    def __str__(self):
        return self.peso   