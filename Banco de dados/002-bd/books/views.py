from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import Cad_livros
from .models import livros

def cadastro(request):
        form = Cad_livros()
        context = {
            'form': form
        }

        return render(request, 'cadastro.html', context=context)
        
        


def estante(request):
    novo_livro = livros()
    novo_livro.livro = request.POST.get('livro')
    novo_livro.autor = request.POST.get('autor')
    novo_livro.categoria = request.POST.get('categoria')
    novo_livro.save()
    
    return HttpResponse('teste')
    
    
