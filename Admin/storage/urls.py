from django.urls import path
from . import views

urlpatterns = [
    path('st/', views.storage, name='storage')
]


