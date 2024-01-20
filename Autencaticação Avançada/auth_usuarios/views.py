from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib import auth

def cadastro(request):
    if request.method == "GET":                     #estou armazenando os dados usando o verbo da 
        return render(request, 'cadastro.html')     #requisição.
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if not senha == confirmar_senha:
            messages.add_message(request, constants.ERROR, 'Senha diferente de confirmar senha')
            return redirect('/auth/cadastro')

        verification_user = User.objects.filter(username=username)

        if verification_user.exists():
            messages.add_message(request, constants.ERROR, 'Usuario já existe')
            return redirect('/auth/cadastro')

        try:   
            User.objects.create_user(
                username=username,
                password=senha
            )
            return redirect('/auth/logar')
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno no servidor')
            return redirect('/auth/cadastro')

def logar(request):
    if request.method == "GET":
        return render(request, 'logar.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        verification_user = auth.authenticate(request, username=username, password=senha)

        if verification_user:
            auth.login(request, verification_user)
            return redirect('/flashcard/novo_flashcard/') #vai dar erro
        else:
            messages.add_message(request, constants.ERROR, 'Usuario ou senha inválidos')
            return redirect('/auth/logar/')


def logout(request):
    auth.logout(request)
    return redirect('/auth/logar')
