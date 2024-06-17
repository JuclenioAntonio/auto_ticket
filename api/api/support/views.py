from rest_framework import permissions, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import utils

from . import models, serializers, utils




def handle_query(query: str, pipeline: utils.IPipeline, resolver: utils.IResolver):
    query_features = pipeline.transform(query)
    predicted_category = pipeline.predict(query_features)

    if(predicted_category == 'suporte'):
        answer = resolver.find_answer_in_faq(query)
        if answer is not None:
            return Response({"resposta":answer})
        else:
            return resolver.direct_to_human_agent(query)
    elif predicted_category == 'feedback':
        feedback_category = resolver.categorize_feedback(query)
        resolver.store_feedback(query, feedback_category)
        return resolver.respond_to_customer_with_thanks()

    elif predicted_category == 'ticket':
        ticket_info = resolver.extract_ticket_information(query)
        resolver.create_ticket(ticket_info)
        return resolver.respond_to_customer_with_ticket_number(ticket_info['ticket_number'])
    else:
        return resolver.respond_to_customer_with_error()



@api_view(['POST'])
def query(request):
    query = request.data.get('query',None)

    data = handle_query(query, )
    return Response({"message":"Hello World {query}"})