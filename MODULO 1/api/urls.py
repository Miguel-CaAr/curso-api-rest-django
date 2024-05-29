from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('curso/', views.curso),
    path('curso/crear/', views.crear_curso),
    path('cursodrf/', views.CursoList.as_view())
]
