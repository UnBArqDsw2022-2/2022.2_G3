# Generated by Django 4.1.4 on 2023-01-25 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('cpf', models.CharField(max_length=14, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=75)),
                ('telefone', models.CharField(max_length=15)),
                ('senha', models.CharField(max_length=250)),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1)),
                ('data_nascimento', models.DateField()),
            ],
        ),
    ]