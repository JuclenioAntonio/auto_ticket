from django.db import models


categorias_faq = {
    "GERAL": "Perguntas frequentes gerais",
    "PRODUTO": "FAQ sobre produtos",
    "SERVICO": "FAQ sobre serviços",
}

produtos = {
    "PRODUTOA":"Produto A",
    "PRODUTOB":"Produto B",
    "PRODUTOC":"Produto C",
}

estados = {
    "ATIVO":"Ativo",
    "ARQUIVADO":"Arquivado"
}

canais = {
    "EMAIL":"email",
    "WEBSITE":"website",
    "WHATSAPP":"whatsapp"
}

prioridades = {
    "BAIXA":"Baixa",
    "MEDIA":"Media",
    "ALTA":"Alta"
}

filas = {
    "BASE":"Base",
    "PREMIUM":"Premium",
    "GOLD":"Gold"
}

class FAQ(models.Model):
    pergunta = models.TextField()
    resposta = models.TextField()
    categoria = models.TextField(choices=categorias_faq)
    palavras_chaves = models.TextField()
    produto = models.TextField(choices=produtos)
    estado = models.TextField(choices=estados)

class Feedback(models.Model):
    nome_cliente = models.CharField(max_length=300)
    email = models.EmailField()
    criado_em = models.DateTimeField(auto_now_add=True)
    classificacao = models.IntegerField()
    descricao = models.TextField()
    canal_feedback = models.TextField(choices=canais)
    produto = models.TextField(choices=produtos)

class Ticket(models.Model):
    assunto = models.CharField(max_length=300)
    descricao = models.TextField()
    prioridade = models.TextField(choices=prioridades)
    canal_abertura = models.TextField(choices=canais)
    nome_cliente = models.CharField(max_length=300)
    email = models.EmailField()
    fila = models.TextField(choices=filas)
    estado = models.TextField(choices=estados)
