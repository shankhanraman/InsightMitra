import openai
from vector_storage import store_vector, retrieve_vectors
from database import query_collection

# Set up OpenAI API key
openai.api_key = "your_openai_api_key"

def process_query(query: str):
    # Retrieve relevant vectors
    documents = retrieve_vectors(query)
    
    # Format data for LLM
    prompt = f"Answer the following query based on these documents:\n\nQuery: {query}\nDocuments:\n"
    for doc in documents:
        prompt += f"- {doc}\n"
    
    # Call the LLM for insight generation
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    
    answer = response.choices[0].text.strip()
    
    # Store query in history
    query_collection.insert_one({"query": query, "response": answer})
    
    return {"query": query, "response": answer}
