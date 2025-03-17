from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import AdminCreationForm

# Create your views here.

#Tela de login 
def index(request):
    print("Usuário logado:", request.user.is_authenticated)  # Verifica se a sessão ainda existe
    if request.method == "GET":
        return render(request, 'login/index.html')
    else:        
        email = request.POST.get('email')
        senha = request.POST.get('password')

        user = authenticate(username=email, password=senha)

        if user:
            login(request, user)
            request.session.set_expiry(86400)  # Mantém a sessão por 1 dia
            return redirect('dashboard')
        else:
            return render(request, "login/index.html", {"erro": "Email ou senha incorreto!"})
        

def sair(request):
    logout(request)
    return redirect('login_index')

# Verifica se o usuário é admin antes de acessar a página
def is_admin(user):
    return user.is_staff  # Somente usuários com permissão de staff (admin)

@user_passes_test(is_admin)  # Apenas admins podem acessar
def cadastrar_admin(request):
    if request.method == 'POST':
        form = AdminCreationForm(request.POST)
        if form.is_valid():
            # Formulário válido, salvar o administrador
            form.save()
            messages.success(request, "Novo administrador cadastrado com sucesso!")
            return redirect('cadastrar_admin')  # Redireciona para o painel do admin ou outra página relevante
        else:
            # Exibindo os erros específicos do formulário
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Erro no campo {field}: {error}")
    else:
        form = AdminCreationForm()

    return render(request, 'login/cadastrar_admin.html', {'form': form})

# Função para editar os dados do usuário logado
@login_required
def editar_admin(request):
    user = request.user  # Obtém o usuário logado
    
    # Se o método for POST, significa que estamos enviando o formulário para atualizar
    if request.method == 'POST':
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')

        # Atualiza os dados do usuário
        user.email = email
        user.first_name = first_name
        user.last_name = last_name

         # Verifica se o e-mail fornecido já está cadastrado em outro usuário
        if User.objects.filter(email=email).exclude(id=user.id).exists():
            messages.error(request, "Este e-mail já está cadastrado em outro usuário.")
            return redirect('editar_admin')  # Redireciona para a página de edição novamente com a mensagem de erro

        # Verifica se foi fornecida uma nova senha
        if password:
            user.set_password(password)
        
        user.save()

        messages.success(request, 'Usuário atualizado com sucesso!')
        return redirect('visualizar_admin')  # Redireciona para a mesma página com os dados atualizados

    # Caso o método seja GET, renderizamos o formulário com os dados atuais do usuário
    return render(request, 'login/editar_admin.html', {'user': user})

# Função para visualizar os dados do usuário logado
@login_required
def visualizar_admin(request):
    user = request.user  # Pegando o usuário logado
    return render(request, 'login/visualizar_admin.html', {'user': user})