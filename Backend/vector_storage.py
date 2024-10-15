import pinecone
from openai.embeddings_utils import get_embedding

# Initialize Pinecone
pinecone.init(api_key="your_pinecone_api_key", environment="us-west1-gcp")
index = pinecone.Index("business_analyst_index")

# Store document as vectors
def store_vector(text: str):
    vector = get_embedding(text)
    index.upsert([(text, vector)])

# Retrieve similar vectors
def retrieve_vectors(query: str):
    query_vector = get_embedding(query)
    result = index.query([query_vector], top_k=5)
    documents = [match["id"] for match in result["matches"]]
    return documents
