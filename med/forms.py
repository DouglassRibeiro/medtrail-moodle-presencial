from django import forms
from .models import Pessoa

class PessoaForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Pessoa
        fields = ['nome', 'email', 'senha', 'telefone', 'nascimento', 'genero']