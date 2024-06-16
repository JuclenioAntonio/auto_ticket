# Auto-ticket


## Objetivos:

1. Suporte 24/7: Responder perguntas frequentes e direcionar clientes para os recursos adequados.
2. Categorização de Feedback: Classificar automaticamente o feedback em categorias relevantes pré-definidas.
3. Análise de Tickets: Analisar o conteúdo dos tickets para identificar tipo de problema, urgência e canal de atendimento.
4. Roteamento de Tickets: Utiliza um algoritmo de roteamento para direcionar tickets para os agentes mais adequados.
5. Priorização de Tickets: Priorizar tickets com base na urgência e no impacto no cliente.

## Canais
- Website
- Whatsapp
- Email

## Funcionamento:

1. Recepção de Interação: O cliente pode interagir com o sistema através de chatbots, e-mail ou outros canais.
Processamento da Linguagem Natural: As entradas do cliente são processadas utilizando técnicas de PLN, como tokenização, lematização, análise sintática e semântica.

2. Identificação da Intenção: O sistema identifica a intenção do cliente, como obter suporte, enviar feedback ou abrir um ticket.

3. Roteamento e Resposta:
    1. Suporte 24/7: Se a intenção for obter suporte, o sistema consulta o módulo de FAQ para encontrar respostas para perguntas frequentes. Se a resposta não for encontrada, o sistema direciona o cliente para um agente humano.
    
    2. Categorização de Feedback: Se a intenção for enviar feedback, o sistema utiliza o classificador de feedback para categorizar o feedback e armazená-lo em um banco de dados.

    3. Análise de Tickets: Se a intenção for abrir um ticket, o sistema utiliza o analisador de tickets para extrair informações relevantes e criar o ticket.

    4. Roteamento de Tickets: O roteador de tickets utiliza as informações extraídas pelo analisador de tickets para direcionar o ticket para o agente mais qualificado para lidar com o problema.

    5. Priorização de Tickets: O módulo de priorização classifica os tickets com base na urgência e no impacto no cliente, garantindo que os problemas mais críticos sejam atendidos primeiro.


## Base de Dados
1. FAQs
2. Feedback
3. Ticket
4. Erros
