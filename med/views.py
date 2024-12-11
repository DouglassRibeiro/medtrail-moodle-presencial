from django.shortcuts import render, redirect
from .forms import PessoaForm
from django.contrib import messages

# Create your views here.
def homepage(request):
    return render(request, 'pages/homepage.html')

def homepage_register(request):
    return render(request, 'pages/homepage_register.html')

def just_register(request):
    return render(request, 'pages/just_register.html')

def registrar_pessoa(request):
    if request.method == "POST":
        form = PessoaForm(request.POST)
        if form.is_valid():
            pessoa = form.save(commit=False)
            # Exemplo de como salvar a senha com hash:
            from django.contrib.auth.hashers import make_password
            pessoa.senha = make_password(form.cleaned_data['senha'])
            pessoa.save()
            messages.success(request, "Registro realizado com sucesso!")
            return redirect('pages/homepage.html')  # Altere para o nome da URL desejada
    else:
        form = PessoaForm()
    return render(request, 'pages/register.html', {'form': form})
