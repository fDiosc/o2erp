# Generated by Django 4.0.4 on 2022-06-07 17:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('O2site', '0004_alter_diaria_servico_alter_pessoajuridica_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoafisica',
            name='cadastro',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pessoafisica',
            name='cargo',
            field=models.CharField(blank=True, choices=[('CLT', 'CLT'), ('DIARISTA', 'DIARISTA'), ('CLIENTE', 'CLIENTE')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='pessoafisica',
            name='tipo',
            field=models.CharField(choices=[('CLIENTE', 'CLIENTE'), ('FUNCIONÁRIO', 'FUNCIONÁRIO')], max_length=20),
        ),
    ]
