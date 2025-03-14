from django import forms
from django.contrib.auth.models import User

class AdminCreationForm(forms.ModelForm):
    nome_completo = forms.CharField(max_length=150, required=True, label="Nome Completo")
    email = forms.EmailField(required=True, label="E-mail")
    senha = forms.CharField(widget=forms.PasswordInput, required=True, label="Senha")

    class Meta:
        model = User
        fields = ['nome_completo', 'email', 'senha']

    def save(self, commit=True):
        """Salva o usuário como administrador."""
        user = super().save(commit=False)
        user.username = self.cleaned_data['email'].lower()  # Usa o e-mail como username em minúsculo
        user.email = self.cleaned_data['email'].lower()  # Garante consistência

        # Dividir nome completo em first_name e last_name
        nome_completo = self.cleaned_data['nome_completo'].strip()
        nomes = nome_completo.split(" ", 1)
        user.first_name = nomes[0]
        user.last_name = nomes[1] if len(nomes) > 1 else ""

        user.set_password(self.cleaned_data['senha'])  # Criptografa a senha
        user.is_staff = True  # Define como administrador

        if commit:
            user.save()
        return user
