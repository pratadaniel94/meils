# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('nome_completo', models.CharField(max_length=50, verbose_name='Nome Completo')),
                ('cpf', models.CharField(unique=True, max_length=14, verbose_name='CPF')),
                ('data_nascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('sexo', models.CharField(max_length=10, choices=[('F', 'Feminino'), ('M', 'Masculino')], verbose_name='Sexo')),
                ('estado_civil', models.CharField(max_length=10, choices=[('Solteiro', 'Solteiro'), ('Casado', 'Casado'), ('Divorciado', 'Divorciado'), ('Viuvo', 'Viuvo')], verbose_name='Estado Civil')),
                ('telefone', models.CharField(max_length=19, verbose_name='Telefone')),
                ('logradouro', models.CharField(max_length=150, verbose_name='Logradouro')),
                ('numero_endereco', models.PositiveIntegerField(verbose_name='Número')),
                ('complemento_endereco', models.CharField(max_length=200, verbose_name='Complemento')),
                ('estado', models.CharField(max_length=15, choices=[('AC', 'Acre'), ('SP', 'São Paulo')])),
                ('cidade', models.CharField(max_length=40, verbose_name='Cidade')),
                ('email', models.EmailField(unique=True, max_length=254, verbose_name='E-mail')),
                ('senha', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(6)])),
            ],
        ),
    ]
