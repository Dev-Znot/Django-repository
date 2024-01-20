from django.shortcuts import render
from .forms import cliente # importo o forms do app

def plataforma(request):
    form = cliente() # Instancia a class
    return render(request, 'plataforma.html', {'form':form}) # Envia pro template
