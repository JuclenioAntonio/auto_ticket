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
    api_url = "https://api-inference.huggingface.co/models/meta-llama/Llama-2-7b-chat-hf"
    query = request.data.get('query')


    json_body = {
        "inputs": query,
        "parameters": {"max_new_tokens":256, "top_p":0.9, "temperature":0.7}
        }
    
    data = json.dumps(json_body)
    response = requests.post(api_url, headers=headers, data=data)

    print(f"Error: {response.text}")

    try:
        if response.status_code == 200:
            return Response(data={'response': response.json()['choices'][0]['text']})
        else:
            print(f"Error: {response.text}")
            return Response(data={'response': "Nada foi encontrado, tente novamente"})
    except Exception as er:
        print(er)    
        return Response(data={'response': "Nada foi encontrado, tente novamente"})