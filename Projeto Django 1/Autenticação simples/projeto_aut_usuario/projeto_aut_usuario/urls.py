
from django.contrib import admin
from django.urls import path, include
from app_aut_usuario import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('auth/', include('app_aut_usuario.urls'))
]
