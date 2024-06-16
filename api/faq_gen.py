import random, csv
import pandas as pd

# Define product categories
categories = {
    "computadores": ["Notebook Dell Inspiron 15 3520", "Notebook Lenovo IdeaPad Slim 5", "Macbook Air M2", "PC Gamer Ryzen 5 5600G", "Computador All-in-One HP 24-df0055"],
    "smartphones": ["iPhone 13 Pro Max", "Samsung Galaxy S23 Ultra", "Xiaomi 13 Pro", "Motorola Edge 30 Ultra", "Google Pixel 7 Pro"],
    "tablets": ["iPad Air 5", "Samsung Galaxy Tab S8+", "Lenovo Tab P11 Pro", "Microsoft Surface Pro 8", "Huawei MatePad 11"],
    "televisores": ["Smart TV LG 55UQ7500", "Smart TV Samsung QN90B", "Smart TV TCL C825", "Smart TV Sony X85J", "Smart TV Philco PTV50G71SN"],
    "eletrodomésticos": ["Geladeira Brastemp BRM45AB", "Fogão Consul CFC5VE", "Lavadora de Roupas Samsung WW10T6240BWX", "Micro-ondas LG MS23K3500SW", "Ar Condicionado Split Gree Inverter GS-K25GW-WIFI"],
    "acessórios": ["Fone de Ouvido Bluetooth JBL Live 66NC", "Carregador de Celular Anker PowerCore III Elite 20000mAh", "Smartwatch Apple Watch Series 8", "Teclado Mecânico Logitech G915 TKL Lightspeed", "Mouse Gamer Razer Viper V2 Pro"]
}

# Define question and answer templates
question_templates = [
    "Qual a diferença entre o {produtoA} e o {produtoB}?",
    "Preciso de ajuda para escolher um {categoria_produto}. Quais as recomendações?",
    "O {produto} é compatível com {dispositivo}?",
    "Quanto tempo demora a entrega do {produto}?",
    "Quais as formas de pagamento aceitas?",
    "Como funciona a garantia do {produto}?",
    "Posso devolver o {produto} se não ficar satisfeito?",
    "Qual o horário de funcionamento do atendimento ao cliente?"
]
answer_templates = [
    "A principal diferença entre o {produtoA} e o {produtoB} é {diferença}.",
    "Para te ajudar a escolher o melhor {categoria_produto}, considere os seguintes fatores: {fator1}, {fator2}, {fator3}.",
    "Sim, o {produto} é compatível com {dispositivo}.",
    "O prazo de entrega do {produto} varia de acordo com a sua região, mas geralmente é de {tempo} dias úteis.",
    "Aceitamos as seguintes formas de pagamento: {forma1}, {forma2}, {forma3}.",
    "A garantia do {produto} cobre defeitos de fabricação por {tempo} a partir da data da compra.",
    "Sim, você tem direito de devolver o {produto} no prazo de {tempo} dias corridos a partir da data da compra, desde que esteja na embalagem original e sem sinais de uso.",
    "O atendimento ao cliente funciona de {horario} a {horario} de segunda a sexta-feira."
]

def generate_faq_entry():
    question_template = random.choice(question_templates)
    answer_template = random.choice(answer_templates)
    category = random.choice(list(categories.keys()))
    product_a = random.choice(categories[category])
    product_b = random.choice(categories[category])
    # Ensure product A and B are different unless the template doesn't use them
    if question_template not in ["Qual a diferença entre o {produtoA} e o {produtoB}?"]:
        while product_a == product_b:
            product_b = random.choice(categories[category])
    device = " (ex: smartphone Samsung Galaxy S23)" if "dispositivo" in answer_template else ""
    specific_product = random.choice(categories[category])

    # Define example factors to consider for different categories (replace with more specific details)
    factors = {
        "computadores": [
            "Processador (potência e quantidade de núcleos)",
            "Memória RAM (capacidade para executar programas simultâneos)",
            "Armazenamento (capacidade do HD/SSD e velocidade)"
        ],
        "smartphones": [
            "Tela (tamanho, resolução e tecnologia)",
            "Sistema operacional (atualizações e recursos)",
            "Câmera (quantidade de megapixels, recursos e qualidade de imagem)"
        ],
        "tablets": [
            "Tamanho da tela (mobilidade vs. visualização)",
            "Sistema operacional (compatibilidade com aplicativos)",
            "Bateria (duração de carga para uso)"
        ],
        "televisores": [
            "Tamanho da tela ( polegadas )",
            "Resolução de tela (qualidade de imagem)",
            "Smart TV (recursos de streaming e conectividade)"
        ],
        "eletrodomésticos": [
            "Capacidade (litros/kg para geladeiras, lavadoras etc.)",
            "Consumo de energia (eficiência energética)",
            "Funções e recursos específicos (ex: dispenser de água na geladeira)"
        ],
        "acessórios": [
            "Compatibilidade com dispositivos (verifique se funciona com seu aparelho)",
            "Recursos e funcionalidades (ex: cancelamento de ruído em fones)",
            "Marca e reputação (qualidade e garantia)"
        ]
    }

    difference = "[descrever a diferença entre os produtos]"  # Replace with actual product comparisons
    factor1, factor2, factor3 = random.sample(factors[category], 3)  # Select 3 random factors

    # Fill answer templates with generated content
    if question_template == "Qual a diferença entre o {produtoA} e o {produtoB}?":
        question = question_template.format(produtoA=product_a, produtoB=product_b)
        answer = answer_templates[0].format(produtoA=product_a, produtoB=product_b, diferença=difference)

    elif question_template == "Preciso de ajuda para escolher um {categoria_produto}. Quais as recomendações?": 
        question = question_template.format(categoria_produto=category)  
        answer = answer_templates[1].format(categoria_produto=category, fator1=factor1, fator2=factor2, fator3=factor3)

    elif question_template == "O {produto} é compatível com {dispositivo}?":
        question = question_template.format(produto=specific_product, dispositivo=device)
        answer = answer_templates[2].format(produto=specific_product, dispositivo=device)     

    elif question_template ==  "Quanto tempo demora a entrega do {produto}?":
        question = question_template.format(produto=specific_product)
        answer = answer_templates[3].format(produto=specific_product, tempo=random.randint(7, 30)) 

    elif question_template ==  "Quais as formas de pagamento aceitas?":
        forma1 = "cartão de crédito"
        forma2 = "boleto bancário"
        forma3 = "transferência bancária"

        question = question_template
        answer = answer_templates[4].format(forma1=forma1,forma2=forma2,forma3=forma3)

    elif question_template == "Como funciona a garantia do {produto}?":
        question = question_template.format(produto=specific_product)
        answer = answer_templates[5].format(produto=specific_product, tempo=random.randint(90, 130))

    elif question_template ==  "Posso devolver o {produto} se não ficar satisfeito?":
        question = question_template.format(produto=specific_product)
        answer = answer_templates[6].format(produto=specific_product, tempo=random.randint(90, 130))

    elif question_template == "Qual o horário de funcionamento do atendimento ao cliente?":
        question = question_template
        answer = answer_templates[7].format(horario="09:00")
 
    return question, answer


# Generate 100 FAQ entries and write to CSV file
faq_data = []
for _ in range(100):
  question, answer = generate_faq_entry()
  faq_data.append({"pergunta": question, "resposta": answer})


with open('faq_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['pergunta', 'resposta']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(faq_data)

print("100 FAQ entries generated and saved to faq_data.csv")
