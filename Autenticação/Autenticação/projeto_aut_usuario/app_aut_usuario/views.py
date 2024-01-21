from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')


def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        verification_username = User.objects.filter(username=username).first()

        if verification_username:
            return HttpResponse('username already registered')
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        
        return HttpResponse('registration completed')
        

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        verification_user = authenticate(username=username, password=password)

        if verification_user is not None:
            login_django(request, verification_user)

            return render(request, 'plataforma.html')
        else:
            return HttpResponse('Invalid login')


@login_required(login_url="/auth/login/")
def plataforma(request):
    if request.user.is_authenticated:
        return render(request, 'plataforma.html')




