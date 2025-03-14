from django.db import models

class Produtor(models.Model):
    nome = models.CharField(max_length=100)
    fazenda = models.CharField(max_length=150)
    localizacao = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    ativo = models.BooleanField(default=True)  # Campo para verificar se o produtor está ativo

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)
    contato = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Coleta(models.Model):
    produtor = models.ForeignKey('Produtor', on_delete=models.CASCADE)
    data = models.DateField()  
    quantidade_litros = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.produtor.nome} - {self.quantidade_litros}L"


class Qualidade(models.Model):
    produtor = models.ForeignKey(Produtor, on_delete=models.CASCADE)  
    coleta = models.OneToOneField(Coleta, on_delete=models.CASCADE)
    gordura = models.DecimalField(max_digits=5, decimal_places=2)
    proteina = models.DecimalField(max_digits=5, decimal_places=2)
    contagem_bacteriana = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.CharField(
        max_length=50, 
        choices=[("Aprovado", "Aprovado"), ("Reprovado", "Reprovado")], 
        null=False, 
        blank=False,  # Garante que o campo não pode ficar vazio
        default="Aprovado"  # Adiciona um valor padrão para evitar erros
    )
    ativo = models.BooleanField(default = True)


    def __str__(self):
        return f"Qualidade - {self.coleta.produtor.nome}"


class Pagamento(models.Model):
    produtor = models.ForeignKey(Produtor, on_delete=models.CASCADE)
    data_pagamento = models.DateField(blank=True, null=True)  # Agora a data pode ser inserida manualmente
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    
    METODO_CHOICES = [
        ('Pix', 'Pix'),
        ('Boleto', 'Boleto'),
        ('Transferência', 'Transferência'),
    ]
    metodo_pagamento = models.CharField(max_length=15, choices=METODO_CHOICES)

    def __str__(self):
        return f"Pagamento {self.produtor.nome} - R$ {self.valor}"

class Funcionario(models.Model):
    imagem = models.ImageField(upload_to='funcionarios/', null=True, blank=True) 
    nome = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    funcao = models.CharField(max_length=100)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class Venda(models.Model):
    imagem = models.ImageField(upload_to='vendas/', blank=True, null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_venda = models.DateField()
    quantidade_litros = models.DecimalField(max_digits=10, decimal_places=2)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Venda {self.cliente.nome} - {self.quantidade_litros}L"

class Transporte(models.Model):
    motorista = models.CharField(max_length=100)
    placa = models.CharField(max_length=10, unique=True)
    coleta_quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    destino = models.CharField(max_length=255)
    data_envio = models.DateTimeField(auto_now_add=True)
    data_chegada = models.DateTimeField(blank=True, null=True) 
    status = models.CharField(max_length=50,choices=[("Em andamento", "Em andamento"), ("Concluído", "Concluído"), ("Atraso", "Atraso")],default="Em andamento")
    motivo_atraso = models.TextField(blank=True, null=True) 
    feedback_cliente = models.TextField(blank=True, null=True) 
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"Transporte {self.motorista} - {self.placa} - {self.status}"
