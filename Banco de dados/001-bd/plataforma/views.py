from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import cliente # importo o forms do app
from .models import Cliente

def plataforma(request):
    form = cliente() # Instancia a class
    if request.method == 'GET':
        return render(request, 'plataforma.html', {'form':form}) # Envia pro template
    else:
        return redirect('/app/usuario')


def usuario(request):
    #Salva os dados da tela no banco de dados
    novo_usuario = Cliente()
    novo_usuario.nome = request.POST.get('name')
    novo_usuario.data_nacimento = request.POST.get('data_nacimento')
    novo_usuario.save()
    return HttpResponse('Dados salvos')


