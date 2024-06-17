# Generated by Django 5.0.6 on 2024-06-17 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assunto', models.CharField(max_length=300)),
                ('descricao', models.TextField()),
                ('prioridade', models.TextField(choices=[('BAIXA', 'Baixa'), ('MEDIA', 'Media'), ('ALTA', 'Alta')])),
                ('canal_abertura', models.TextField(choices=[('EMAIL', 'email'), ('WEBSITE', 'website'), ('WHATSAPP', 'whatsapp')])),
                ('nome_cliente', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254)),
                ('fila', models.TextField(choices=[('BASE', 'Base'), ('PREMIUM', 'Premium'), ('GOLD', 'Gold')])),
                ('estado', models.TextField(choices=[('ATIVO', 'Ativo'), ('ARQUIVADO', 'Arquivado')])),
            ],
        ),
    ]
