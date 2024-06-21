# Auto-ticket


## Objetivos:

1. Suporte 24/7: Responder perguntas frequentes e direcionar clientes para os recursos adequados.

## Canais
- Website


## Funcionamento:

1. Recepção de Interação: O cliente pode interagir com o sistema através de chatbots, e-mail ou outros canais.
Processamento da Linguagem Natural: As entradas do cliente são processadas utilizando técnicas de PLN, como tokenização, lematização, análise sintática e semântica.

2. Identificação da Intenção: O sistema identifica a intenção do cliente, como obter suporte, enviar feedback ou abrir um ticket.


## Base de Dados
1. FAQs
2. Feedback


### Instalação do projecto

1. Fazer o clone da aplicação usando o git `git clone https://github.com/JuclenioAntonio/auto_ticket.git`
2. Configurar API
   1. Instalar as dependências do projecto
      - `> cd auto_ticket/api/`
      - `> poetry shell`
      - `> poetry install`
   2. Instalar dependências do modelo LLM
      - `> cd auto_ticket/api/`
      - `> poetry shell`
      - `> llm install llm-gpt4all`
      - `> llm -m orca-mini-3b-gguf2-q4_0 "What is Large Language Model?"`
   3. Configurar a base de dados vetorizada
      - `> docker pull epsilla/vectordb`
      - `> docker run --pull=always -d -p 8888:8888 epsilla/vectordb`
   4. Testar base de dados vetorizada
      - `> cd auto_ticket/api/src`
      - `> poetry shell`
      - `> python learn.py`
   5. Testar o chatbot
      - `> cd auto_ticket/api/src`
      - `> poetry shell`
      - `> streamlit run app.py`
   6. Rodar a API
      - `> cd auto_ticket/api/support`
      - `> poetry shell`
      - `> python manage.py runserver`
3. Configurar o front-end
   1. `> cd auto_ticket/web`
   2. `> npm install`
   3. `> npm run dev`

