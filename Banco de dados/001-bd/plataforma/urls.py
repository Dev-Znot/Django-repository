from django.urls import path
from . import views

urlpatterns = [
    path('plataforma/', views.plataforma, name='plataforma'),
    path('usuario/', views.usuario, name='usuario'),
]
