from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re

class AdminCreationForm(forms.ModelForm):
    nome_completo = forms.CharField(
        max_length=150,
        required=True,
        label="Nome Completo",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome completo'})
    )
    email = forms.EmailField(
        required=True,
        label="E-mail",
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Digite o e-mail'})
    )
    senha = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite a senha'}),
        required=True,
        label="Senha"
    )
    confirmar_senha = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirme a senha'}),
        required=True,
        label="Confirmar Senha"
    )

    class Meta:
        model = User
        fields = ['nome_completo', 'email', 'senha']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(username=email).exists():
            raise ValidationError("Este e-mail já está cadastrado como administrador.")
        return email
    
    def clean_senha(self):
        senha = self.cleaned_data.get("senha")

        # Verifica se a senha tem pelo menos 8 caracteres e inclui pelo menos uma letra e um número
        if not re.match(r'^(?=.*[A-Za-z])(?=.*\d).{8,}$', senha):
            raise ValidationError("A senha deve ter pelo menos 8 caracteres, incluindo letras e números.")

        return senha

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get("senha")
        confirmar_senha = cleaned_data.get("confirmar_senha")

        if senha and confirmar_senha and senha != confirmar_senha:
            raise ValidationError("As senhas não coincidem. Por favor, tente novamente.")

        return cleaned_data

    def save(self, commit=True):
        email = self.cleaned_data['email']
        
        user = super().save(commit=False)
        user.username = email  
        
        nome_completo = self.cleaned_data['nome_completo'].strip()
        if " " in nome_completo:
            user.first_name, user.last_name = nome_completo.split(" ", 1)
        else:
            user.first_name = nome_completo
            user.last_name = ""

        user.set_password(self.cleaned_data['senha'])  # Define a senha criptografada
        user.is_staff = True  # O usuário será um administrador

        if commit:
            user.save()
        return user
