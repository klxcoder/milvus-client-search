from pymilvus import MilvusClient
from embedding import encode_queries, get_dimension
from docs import read_docs_to_list
from chat import chat

INPUT_FILE = 'docs.txt'

client = MilvusClient("milvus_demo.db")

# Create a collection

if client.has_collection(collection_name="demo_collection"):
    client.drop_collection(collection_name="demo_collection")
client.create_collection(
    collection_name="demo_collection",
    dimension=get_dimension(),
)

docs = read_docs_to_list(INPUT_FILE)

print(f'Read {len(docs)} lines from {INPUT_FILE}')

vectors = encode_queries(docs)

data = [
    {"id": i, "vector": vectors[i], "text": docs[i]}
    for i in range(len(vectors))
]

res = client.insert(collection_name="demo_collection", data=data)

print(res)

while True:
    print('-'*100)
    query = input("Question: ")
    if query=="":
        print("Empty question -> Stop the program")
        break
    query_vectors = encode_queries([query])
    res = client.search(
        collection_name="demo_collection",
        data=query_vectors,
        limit=10,
        output_fields=["text"],
    )
    print('Answer: ', end = "")
    rag_data = [entity['entity']['text'] for entity in res[0]]
    chat(query, rag_data)
    print("")