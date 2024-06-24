from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests, json

# 
from langchain.vectorstores import Epsilla
from pyepsilla import vectordb
from sentence_transformers import SentenceTransformer

import subprocess as st
from typing import List

from . import models, serializers
# Create your views here.

model = SentenceTransformer('all-MiniLM-L6-v2')


class LocalEmbeddings():
    def embed_query(self, text: str) -> List[float]:
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
    token_access = "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"
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