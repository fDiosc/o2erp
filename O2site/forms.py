from django import forms
from . import models

class Diarias(forms.ModelForm):
    class Meta:
        model = models.Diaria
        fields = "__all__"

class PessoaFisica(forms.ModelForm):
    class Meta:
        model = models.PessoaFisica
        fields = "__all__"

class PessoaJuridica(forms.ModelForm):
    class Meta:
        model = models.PessoaJuridica
        fields = "__all__"

class Contrato(forms.ModelForm):
    class Meta:
        model = models.Contrato
        fields = "__all__"

class Servico(forms.ModelForm):
    class Meta:
        model = models.Servico
        fields = "__all__"