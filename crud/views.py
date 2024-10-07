from django.shortcuts import render, redirect, get_object_or_404
from .models import Pessoa, Beneficiario

def home(request):
    pessoas = Pessoa.objects.all
    return render(request, "index.html", {"pessoas": pessoas})

def salvar(request):
    vnome = request.POST.get("nome")
    Pessoa.objects.create(nome=vnome)
    pessoas = Pessoa.objects.all()
    return render(request, "index.html", {"pessoas": pessoas})

def editar(request, id):
    pessoa = Pessoa.objects.get(id=id)
    return render(request, "update.html", {"pessoa": pessoa})

def update(request, id):
    vnome = request.POST.get("nome")
    pessoa = Pessoa.objects.get(id=id)
    pessoa.nome = vnome
    pessoa.save()
    return redirect(home)

def delete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    pessoa.delete()
    return redirect(home)

# beneficiarios
def lista_beneficiarios(request):
    beneficiarios = Beneficiario.objects.all()
    return render(request, "lista_beneficiarios.html", {"beneficiarios": beneficiarios})

def salvar_beneficiario(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        apelido = request.POST.get("apelido")
        documento = request.POST.get("documento")
        endereco = request.POST.get("endereco")
        telefone = request.POST.get("telefone")
        observacoes = request.POST.get("observacoes")
        Beneficiario.objects.create(nome=nome, apelido=apelido, documento=documento, endereco=endereco, telefone=telefone, observacoes=observacoes)
        return redirect(lista_beneficiarios)
    return render(request, "form_beneficiario.html")

def editar_beneficiario(request, id):
    beneficiario = get_object_or_404(Beneficiario, id=id)
    return render(request, "update_beneficiario.html", {"beneficiario": beneficiario})

def update_beneficiario(request, id):
    beneficiario = get_object_or_404(Beneficiario, id=id)
    if request.method == "POST":
        beneficiario.nome = request.POST.get("nome")
        beneficiario.apelido = request.POST.get("apelido")
        beneficiario.documento = request.POST.get("documento")
        beneficiario.endereco = request.POST.get("endereco")
        beneficiario.telefone = request.POST.get("telefone")
        beneficiario.observacoes = request.POST.get("observacoes")
        beneficiario.save()
        return redirect(lista_beneficiarios)

def delete_beneficiario(request, id):
    beneficiario = get_object_or_404(Beneficiario, id=id)
    beneficiario.delete()
    return redirect(lista_beneficiarios)