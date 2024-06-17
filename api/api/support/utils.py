from abc import ABC, abstractmethod
from .models import FAQ, Feedback, Ticket

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


class IPipeline(ABC):
    @abstractmethod
    def transform(self, data):
        pass

    @abstractmethod
    def predict(self, data):
        pass

    @abstractmethod
    def get_pipeline(self):
        pass


class IResolver(ABC):
    @abstractmethod
    def find_answer_in_faq(self,query):
    # ... (implementar lógica para encontrar a resposta mais relevante na FAQ)
        ...
    @abstractmethod
    def direct_to_human_agent(self,query):
        # ... (implementar lógica para direcionar o cliente para um agente humano)
        ...

    @abstractmethod
    def categorize_feedback(self,query):
        # ... (implementar lógica para categorizar o feedback)
        ...
    @abstractmethod
    def store_feedback(self,query, feedback_category):
        # ... (implementar lógica para armazenar o feedback no banco de dados)
        ...
    @abstractmethod
    def respond_to_customer_with_thanks(self):
        # ... (implementar mensagem de agradecimento ao cliente)
        ...
    @abstractmethod
    def extract_ticket_information(self,query):
        # ... (implementar lógica para extrair informações do ticket da consulta)
        ...
    @abstractmethod
    def create_ticket(self,ticket_info):
        # ... (implementar lógica para criar o ticket no sistema de suporte)
        ...
    @abstractmethod
    def respond_to_customer_with_ticket_number(self,ticket_number):
        # ... (implementar mensagem para o cliente com o número do ticket)
        ...
    @abstractmethod
    def respond_to_customer_with_error(self):
        # ... (implementar mensagem de erro para o cliente)
        ...


class InitPipepline(IPipeline):
    def transform(self, data):
        return {"data":"some data"}
    
    def predict(self, data):
        return {"categoria":"suporte"}

    @abstractmethod
    def get_pipeline(self):
        return {"pipeline":"somepipeline"}


def process_query(query):
  query = query.lower()
  query = query.translate(str.maketrans('', '', string.punctuation))
  return query

def extract_keywords(query):
  stop_words = set(stopwords.words('portuguese'))
  words = word_tokenize(query)
  keywords = [word for word in words if word not in stop_words and len(word) >= 3]
  return keywords

class InitResolver(IResolver):
    def find_answer_in_faq(self,query):
    # ... (implementar lógica para encontrar a resposta mais relevante na FAQ
        processed_query = process_query(query)
        keywords = extract_keywords(processed_query)

        # Perform keyword matching using the "palavras_chaves" field
        matching_faqs_by_keywords = FAQ.objects.filter(palavras_chaves__in=keywords)

        # If keywords match, further refine by text similarity
        if matching_faqs_by_keywords.exists():
            similar_faqs = []
            for faq in matching_faqs_by_keywords:
                # Use a text similarity metric like cosine similarity or Jaccard similarity
                # to compare the query and the FAQ's pergunta (question) field
                similarity_score = calculate_text_similarity(processed_query, faq.pergunta)
                if similarity_score > 0.5:  # Adjust threshold as needed
                    similar_faqs.append((faq, similarity_score))

            # If similar FAQs exist, select the one with the highest similarity score
            if similar_faqs:
                top_faq, top_similarity_score = max(similar_faqs, key=lambda x: x[1])
                return top_faq.resposta
            else:
                # If no similar FAQs found, use category matching
                return refine_answer_by_category(processed_query, matching_faqs_by_keywords)

        # If no keyword matches, refine by category matching
        else:
            return refine_answer_by_category(processed_query, None)

    def direct_to_human_agent(self,query):
        # ... (implementar lógica para direcionar o cliente para um agente humano)
        ...

    def categorize_feedback(self,query):
        if "problema" in query or "erro" in query:
            return "Problema"
        elif "sugestão" in query or "melhorar" in query:
            return "Sugestão"
        else:
            return "Geral"
 
    def store_feedback(self,query, feedback_category, email, nome):
        name = nome  
        email = email 
        description = process_query(query) 

        feedback = Feedback(
            nome_cliente=name,
            email=email,
            descricao=description,
            canal_feedback="WEBSITE", 
            produto="GERAL", 
            classificacao=None,  
        )
        feedback.save()

    def respond_to_customer_with_thanks(self):
        message = "Obrigado por entrar em contato! Estamos felizes em poder ajudar."
        return message
 
    def extract_ticket_information(self,query):
        # ... (implementar lógica para extrair informações do ticket da consulta)
        ...
 
    def create_ticket(self,ticket_info):
        # ... (implementar lógica para criar o ticket no sistema de suporte)
        ...

    def respond_to_customer_with_ticket_number(self,ticket_number):
        # ... (implementar mensagem para o cliente com o número do ticket)
        ...

    def respond_to_customer_with_error(self):
        # ... (implementar mensagem de erro para o cliente)
        ...