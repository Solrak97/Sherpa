from langchain_community.vectorstores import Qdrant
from qdrant_client import QdrantClient
from qdrant_client.http.models import VectorParams, Distance
from ollama_embeddings import OllamaEmbeddings

documents = [
    "Sherpa connects natural language to SQL.",
    "LangChain lets you build LLM apps.",
    "Qdrant is a fast and scalable vector store.",
]


embedding_model = OllamaEmbeddings(
    model_name="mxbai-embed-large",
    base_url="http://localhost:11434"
)


qdrant = QdrantClient(
    host="localhost",
    port=6333
)

collection = "sherpa_docs"

if not qdrant.collection_exists(collection):
    qdrant.create_collection(
        collection,
        vectors_config=VectorParams(
            size=len(embedding_model.embed_query("query")),
            distance=Distance.COSINE
        )
    )

vectorstore = Qdrant(
    client=qdrant,
    collection_name=collection,
    embeddings=embedding_model
)

vectorstore.add_texts(documents)




query = "What can I use for semantic search?"
results = vectorstore.similarity_search(query, k=2)

for doc in results:
    print("🔍", doc.page_content)