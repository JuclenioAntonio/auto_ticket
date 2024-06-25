'''
    Controladores para gestão de feedback e atendimento ao cliente com FAQ
'''
from typing import List
import os
import requests
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from langchain.vectorstores import Epsilla
from pyepsilla import vectordb
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv

from . import models, serializers



model = SentenceTransformer('all-MiniLM-L6-v2')
load_dotenv()

class LocalEmbeddings():
    '''Conversão e consulta na base de dados vetorizada'''
    def embed_query(self, text: str) -> List[float]:
        ''' Converte a consulta em lista de ids'''
        return model.encode(text).tolist()

embeddings = LocalEmbeddings()

client = vectordb.Client()
vectordb_store = Epsilla(
    client,
    embeddings,
    db_path="/tmp/localchatdb",
    db_name="LocalChatDB",
)

vectordb_store.use_collection("LocalChatCollection")

class FeedbackViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.Feedback.objects.all()
    serializer_class = serializers.FeedbackSerializer
    permission_classes = [permissions.AllowAny]

@api_view(['POST'])
def queryset_faq(request):
    token_access = os.getenv('HUGGINGFACE_API_TOKEN')
    headers = {'Authorization': f'Bearer {token_access}', 'Content-Type': 'application/json'  }
    api_url = "https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-70B-Instruct"
    query = request.data.get('query')

    context = '\n'.join(map(lambda doc: doc.page_content, vectordb_store.similarity_search(request.data.get('query'), k = 5)))

    prompt = f'''
    Responda à pergunta com base no contexto fornecido, Dê respostas com até 250 caracteres. Tente entender o contexto e reformule a pergunta.
    Não invente coisas nem diga coisas não mencionadas no contexto. Peça não mais informações quando necessário. Responda em Português.

    Contexto:
    {context}

    Pergunta:
    {query}

    Resposta:
    '''

    
    print(prompt)
    json_body = {"inputs": prompt}
    response = requests.post(api_url, headers=headers, json=json_body)    
    try:
        if response.status_code == 200:
            data = response.json()
            answer = data[0]["generated_text"].split('\n')
            print(answer)
            return Response(data={'response': answer[-1]})
        else:
            return Response(data={'response': "Nada foi encontrado, tente novamente"})
    except Exception as er:  
        return Response(data={'response': "Nada foi encontrado, tente novamente1"})