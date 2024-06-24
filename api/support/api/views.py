from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests, json

from . import models, serializers
# Create your views here.


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

    json_body = {"inputs": query + "responda em Português.",}
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