import joblib
from actions import (find_answer_in_faq, respond_to_customer_with_error,respond_to_customer_with_thanks,respond_to_customer_with_ticket_number,
                     respond_to_customer, direct_to_human_agent, categorize_feedback, store_feedback, extract_ticket_information, create_ticket)

filename = "data/model.pkl"
pipeline = joblib.load(filename) 

def handle_customer_query(query):
    # Processar a consulta do cliente
    query_features = pipeline.transform([query])

    # Prever a categoria da consulta
    predicted_category = pipeline.predict(query_features)

    # Responder de acordo com a categoria prevista
    if predicted_category == 'suporte':
        answer = find_answer_in_faq(query)
        if answer is not None:
            respond_to_customer(answer)
        else:
            direct_to_human_agent(query)
    elif predicted_category == 'feedback':
        feedback_category = categorize_feedback(query)
        store_feedback(query, feedback_category)
        respond_to_customer_with_thanks()

    elif predicted_category == 'ticket':
        ticket_info = extract_ticket_information(query)
        create_ticket(ticket_info)
        respond_to_customer_with_ticket_number(ticket_info['ticket_number'])
    else:
        respond_to_customer_with_error()
