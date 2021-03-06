from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class PessoaFisica(models.Model):
    PF_TIPO = (
        ("CLIENTE", "CLIENTE"),
        ("FUNCIONÁRIO", "FUNCIONÁRIO"),
     )
      
    PF_CARGO = (
        ("CLT", "CLT"),
        ("DIARISTA", "DIARISTA"),
        ("CLIENTE", "CLIENTE"),
     )

    nome = models.CharField(blank=False, max_length=100)
    cpf = models.CharField(blank=False, max_length=20)
    endereco = models.CharField(blank=True, max_length=200)
    email = models.CharField(blank=True, max_length=50)
    telefone = models.CharField(blank=True, max_length=20)
    tipo = models.CharField(blank=False, choices=PF_TIPO, null=False, max_length=20) # cliente, funcionário, etc
    cargo = models.CharField(blank=True, choices=PF_CARGO, null=True, max_length=20) # ASG
    cadastro = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Nome: {self.nome}, Tipo: {self.tipo}, cargo: {self.cargo}, Data de cadastro: {self.cadastro}"

class PessoaJuridica(models.Model):
    PJ_CHOICES = (
        ("CLIENTE", "CLIENTE"),
        ("FORNECEDOR", "FORNECEDOR"),
    )

    razao_social = models.CharField(blank=False, max_length=100)
    cnpj = models.CharField(blank=False, max_length=30)
    endereco = models.CharField(blank=True, max_length=200)
    email = models.CharField(blank=True, max_length=50)
    telefone = models.CharField(blank=True, max_length=20)
    tipo = models.CharField(blank=False, choices=PJ_CHOICES, null=False, max_length=20) # cliente, fornecedor, etc
    pessoafisica = models.ManyToManyField(PessoaFisica, blank=True, related_name="PessoasJuridicas")
    

    def __str__(self):
        return self.razao_social

class Servico(models.Model):
    pessoafisica = models.ForeignKey('PessoaFisica', blank=True, on_delete=models.CASCADE)
    pessoajuridica = models.ForeignKey('PessoaJuridica', blank=True, on_delete=models.CASCADE)
    tag = models.CharField(blank=True, max_length=50)
    contrato = models.ForeignKey('Contrato', on_delete=models.CASCADE)
    qtd_asg = models.IntegerField(blank=False)
    observacao = models.TextField(blank=True)
    endereco = models.CharField(blank=False, max_length=200)
    ativo = models.BooleanField(default=True)
    

    def __str__(self):
        return f"Cliente: {self.pessoajuridica.razao_social}, Tipo: {self.tag}, Contrato: {self.contrato.n_ct}, Data Início: {self.contrato.data_inicio}, Previsão de execução: até {self.contrato.previsao_execucao} dias, Qtd ASG TOTAL: {self.qtd_asg}, Ativo: {self.ativo}"

class Diaria(models.Model):
    DIARIA_CHOICES = (
        ("N", "NÃO"),
        ("T", "TRANSPORTE"),
        ("A", "ALIMENTAÇÃO"),
        ("AM", "ALIMENTAÇÃO + TRANSPORTE")
    )

    pessoafisica = models.ForeignKey('PessoaFisica', on_delete=models.CASCADE)
    servico = models.ForeignKey('Servico', blank=False, on_delete=models.CASCADE)
    nome = models.CharField(blank=True, max_length=100)
    choices = models.CharField(blank=False, choices=DIARIA_CHOICES, null=False, max_length=2)
    data = models.DateTimeField(null=False, blank=False)
    observacao = models.TextField(blank=True)
    paga = models.BooleanField(default=False)

    def __str__(self):
        return f"Nome: {self.pessoafisica.nome}, Serviço: {self.servico}, Data: {self.data}, Detalhes: {self.choices}, Pago: {self.paga}"

class Contrato(models.Model):
    pessoafisica = models.ForeignKey('PessoaFisica', blank=True, on_delete=models.CASCADE)
    pessoajuridica = models.ForeignKey('PessoaJuridica', blank=True, on_delete=models.CASCADE)
    n_ct = models.CharField(blank=False, max_length=20)
    area = models.IntegerField(blank=False)
    valor = models.FloatField(blank=False)
    data_inicio = models.DateField(blank=False)
    previsao_execucao = models.IntegerField(blank=False)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"Empresa: {self.pessoajuridica}, Ct. num: {self.n_ct}, Área: {self.area}, Data de início: {self.data_inicio}, Previsão: {self.previsao_execucao}, Valor: {self.valor}, Endereço: {self.pessoajuridica.endereco}"