from django.db import models

class Cliente(models.Model): #Cria-se o banco de dados com as respectivas info
    nome = models.CharField(max_length=20)
    data_nacimento = models.DateField()
    email = models.EmailField()
    descricao = models.CharField(max_length=100)

    #Aplica-se o makemigrations e migrate
