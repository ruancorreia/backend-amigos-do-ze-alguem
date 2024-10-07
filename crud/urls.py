from django.contrib import admin
from django.urls import path, include
from .views import (
    home, salvar, editar, update, delete,
    lista_beneficiarios, salvar_beneficiario, editar_beneficiario,
    update_beneficiario, delete_beneficiario
)

urlpatterns = [
    path('', home),
    path('salvar/', salvar, name='salvar'),
    path('editar/<int:id>', editar, name='editar'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name='delete'),
    
# Beneficiarios
    path('beneficiarios/', lista_beneficiarios, name='lista_beneficiarios'),
    path('beneficiarios/salvar/', salvar_beneficiario, name='salvar_beneficiario'),
    path('beneficiarios/editar/<int:id>/', editar_beneficiario, name='editar_beneficiario'),
    path('beneficiarios/update/<int:id>/', update_beneficiario, name='update_beneficiario'),
    path('beneficiarios/delete/<int:id>/', delete_beneficiario, name='delete_beneficiario'),
]


