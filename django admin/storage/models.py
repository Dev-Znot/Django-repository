from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Produtos(models.Model):
    nome = models.CharField(max_length=50)
    valor = models.IntegerField()
    categoria = models.ForeignKey("categoria", on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

