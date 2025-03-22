import random
import requests

EMBEDDING_MODEL = "all-minilm"

def get_dimension():
    response = requests.post(
        "http://localhost:11434/api/show",
        json={"model": EMBEDDING_MODEL}
    )
    response.raise_for_status()  # Ensure request success
    return response.json().get('model_info').get('bert.embedding_length')

# def encode_query(query):
#     return [random.uniform(-1, 1) for _ in range(DIMENSION)]

def encode_query(query):
    response = requests.post(
        "http://localhost:11434/api/embed",
        json={"model": EMBEDDING_MODEL, "input": query}
    )
    response.raise_for_status()  # Ensure request success
    return response.json().get('embeddings')[0]

def encode_queries(queries):
    return [encode_query(query) for query in queries]

if __name__ == '__main__':
    query_vectors = encode_queries(["Who is Alan Turing?"])
    print(query_vectors)
    print(len(query_vectors[0]))
    print(get_dimension())
