from django.shortcuts import render, redirect
from django. urls import reverse_lazy
from accounts.forms import  CadastroForms, CustomLoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages, auth
from django.contrib.auth import get_user_model
User = get_user_model()


def login(request):
    form = CustomLoginForm()

    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        print(f"Vindo aqui00")
        if form.is_valid():
            print(f"Vindo aqui77")
            username = form.cleaned_data["username"] 
            password = form.cleaned_data["password"]

            usuario = authenticate(
                request,
                username=username,
                password=password
            )
            if usuario is not None:
                aviso = 'Login efetuado com sucesso!'
                auth.login(request, usuario)
                messages.success(request, aviso)
                return redirect('list_debtors')
            else:
                print(f"Vindo aqui2")
                messages.error(request, 'Login inválido! Dados incorretos.')
        else:
            print(f"Vindo aqui999")

    
    return render(request, "template/registration/login.html", {"form": form})


def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)

        if form.is_valid():
            nome = form.cleaned_data["nome_cadastro"]
            senha = form.cleaned_data["senha"]
            
            if User.objects.filter(username=nome).exists():
                messages.error(request, "Esse nome de usuário já está em uso.")
                return render(request, "template/registration/cadastro.html", {"form": form})

            usuario = User.objects.create_user(
                username=nome,
                password=senha
            )
            usuario.is_active = True
            usuario.save()
            aviso = 'Cadastro efetuado com sucesso!'
            messages.success(request, aviso)
            return redirect('accounts:login')
        else:
            print(form.errors)
    
    return render(request, "registration/cadastro.html", {"form": form})


def logout(request):
    auth.logout(request)
    messages.success(request, "Deslogado com sucesso!")
    return redirect('accounts:login')

