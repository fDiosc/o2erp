# Generated by Django 4.0.4 on 2022-06-07 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('O2site', '0002_contrato_ativo_diaria_paga_servico_ativo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pessoajuridica',
            name='fornecimento',
        ),
    ]