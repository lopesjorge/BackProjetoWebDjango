from django.db import models


class Agricultor (models.Model):
    Nome = models.CharField(max_length=100)
    CPF = models.IntegerField(max_length=11)
    Telefone = models.IntegerField(max_length=11)


class Propriedade(models.Model):
    Nome = models.CharField(max_length=100)
    Proprietario = models.IntegerField(max_length=11)
    Area = models.IntegerField(max_length=20)


class Colheita (models.Model):
    Tipo = models.CharField(max_length=50)
    Quantidade = models.DecimalField(max_digits=15, decimal_places=2)
    AnoDaColheita = models.IntegerField(max_length=10)


class Motorista(models.Model):
    Nome = models.CharField(max_length=100)
    Matricula = models.IntegerField(max_length=11)
    CNH = models.IntegerField(max_length=11)
    Categoria = models.CharField(max_length=1)


class Veiculo(models.Model):
    Modelo = models.CharField(max_length=50)
    Marca = models.CharField(max_length=50)
    AnoDeFabricacao = models.IntegerField(max_length=10)


class Endereco(models.Model):
    CEP = models.IntegerField(max_length=8)
    Cidade = models.CharField(max_length=50)
    Bairro = models.CharField(max_length=50)
    Rua = models.CharField(max_length=50)
    Numero = models.CharField(max_length=50)


def __str__(self):
    return self.description
