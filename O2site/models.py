from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class PessoaFisica(models.Model):
    nome = models.CharField(blank=False, max_length=100)
    cpf = models.CharField(blank=False, max_length=20)
    endereco = models.CharField(blank=True, max_length=200)
    email = models.CharField(blank=True, max_length=50)
    telefone = models.CharField(blank=True, max_length=20)
    tipo = models.CharField(blank=False, max_length=20) # cliente, funcionário, etc
    cargo = models.CharField(blank=False, max_length=40) # ASG

    def __str__(self):
        return self.nome

class PessoaJuridica(models.Model):
    razao_social = models.CharField(blank=False, max_length=100)
    cnpj = models.CharField(blank=False, max_length=30)
    endereco = models.CharField(blank=True, max_length=200)
    email = models.CharField(blank=True, max_length=50)
    telefone = models.CharField(blank=True, max_length=20)
    tipo = models.CharField(blank=False, max_length=20) # cliente, fornecedor, etc
    pessoafisica = models.ManyToManyField(PessoaFisica, blank=True, related_name="PessoasJuridicas")
    fornecimento = models.CharField(blank=False, max_length=40) # Mat. limpeza, Mat. construção, Combustíveis

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
    

    def __str__(self):
        return f"Cliente: {self.pessoajuridica.razao_social}, Tipo: {self.tag}, Contrato: {self.contrato.n_ct}, Data Início: {self.contrato.data_inicio}, Previsão de execução: até {self.contrato.previsao_execucao} dias, Qtd ASG TOTAL: {self.qtd_asg}"

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
    servico = models.CharField(blank=False, max_length=100)
    choices = models.CharField(blank=False, choices=DIARIA_CHOICES, null=False, max_length=2)
    data = models.DateTimeField(null=False, blank=False)
    observacao = models.TextField(blank=True)

    def __str__(self):
        return f"Nome: {self.pessoafisica.nome}, Serviço: {self.servico}, Data: {self.data}, Detalhes: {self.choices}"

class Contrato(models.Model):
    pessoafisica = models.ForeignKey('PessoaFisica', blank=True, on_delete=models.CASCADE)
    pessoajuridica = models.ForeignKey('PessoaJuridica', blank=True, on_delete=models.CASCADE)
    n_ct = models.CharField(blank=False, max_length=20)
    area = models.IntegerField(blank=False)
    valor = models.FloatField(blank=False)
    data_inicio = models.DateField(blank=False)
    previsao_execucao = models.IntegerField(blank=False)

    def __str__(self):
        return f"Empresa: {self.pessoajuridica}, Ct. num: {self.n_ct}, Área: {self.area}, Data de início: {self.data_inicio}, Previsão: {self.previsao_execucao}, Valor: {self.valor}, Endereço: {self.pessoajuridica.endereco}"