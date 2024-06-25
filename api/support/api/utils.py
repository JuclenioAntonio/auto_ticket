from langchain.vectorstores import Epsilla
from pyepsilla import vectordb
from sentence_transformers import SentenceTransform

model = SentenceTransformer('all-MiniLM-L6-v2')

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