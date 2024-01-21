from django.shortcuts import render
from .forms import Cadastro

def cadastro(request):
    form = Cadastro()
    return render(request, 'cadastro.html', {'form': form} )
