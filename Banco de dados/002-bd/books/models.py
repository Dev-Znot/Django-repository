from django.db import models



class livros(models.Model):
    LIVROS_CHOICES = (
    ('R', 'Romance'),
    ('T', 'Terror'),
    )
    livro = models.CharField(max_length=30)
    autor = models.CharField(max_length=20)
    categoria = models.CharField(max_length=1, choices=LIVROS_CHOICES)
