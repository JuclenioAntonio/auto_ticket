from langchain.vectorstores import Epsilla
from pyepsilla import vectordb
from sentence_transformers import SentenceTransformer
import streamlit as st

import subprocess
from typing import List

# Local embedding model for embedding the question.
model = SentenceTransformer('all-MiniLM-L6-v2')

class LocalEmbeddings():
  def embed_query(self, text: str) -> List[float]:
    return model.encode(text).tolist()

embeddings = LocalEmbeddings()

# Connect to Epsilla as knowledge base.
client = vectordb.Client()
vector_store = Epsilla(
  client,
  embeddings,
  db_path="/tmp/localchatdb",
  db_name="LocalChatDB"
)
vector_store.use_collection("LocalChatCollection")

# The 1st welcome message
st.title("💬 Chatbot")
if "messages" not in st.session_state:
  st.session_state["messages"] = [{"role": "assistant", "content": "Olá! Como posso ajudá-lo?"}]

# A fixture of chat history
for msg in st.session_state.messages:
  st.chat_message(msg["role"]).write(msg["content"])

# Answer user question upon receiving
if question := st.chat_input():
  st.session_state.messages.append({"role": "user", "content": question})

  context = '\n'.join(map(lambda doc: doc.page_content, vector_store.similarity_search(question, k = 5)))

  st.chat_message("user").write(question)

  # Here we use prompt engineering to ingest the most relevant pieces of chunks from knowledge into the prompt.
  prompt = f'''
    Responda à pergunta com base no contexto fornecido. Tente entender o contexto e reformule a pergunta.
    Não invente coisas nem diga coisas não mencionadas no contexto. Peça mais informações quando necessário.

    Contexto:
    {context}

    Pergunta:
    {question}

    Resposta:
    '''
  print(prompt)

  # Call the local LLM and wait for the generation to finish. This is just a quick demo and we can improve it
  # with better ways in the future.
  command = ['llm', '-m', 'orca-mini-3b-gguf2-q4_0', prompt]
  process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
  content = ''
  while True:
    output = process.stdout.readline()
    if output:
      content = content + output
    return_code = process.poll()
    if return_code is not None:
      break

  # Append the response
  msg = { 'role': 'assistant', 'content': content }
  st.session_state.messages.append(msg)
  st.chat_message("assistant").write(msg['content'])