from pymilvus import MilvusClient
from embedding import encode_queries, DIMENSION

client = MilvusClient("milvus_demo.db")

# Create a collection

if client.has_collection(collection_name="demo_collection"):
    client.drop_collection(collection_name="demo_collection")
client.create_collection(
    collection_name="demo_collection",
    dimension=DIMENSION,
)

docs = [
    "Artificial intelligence was founded as an academic discipline in 1956.",
    "Alan Turing was the first person to conduct substantial research in AI.",
    "Born in Maida Vale, London, Turing was raised in southern England.",
]

vectors = encode_queries(docs)

data = [
    {"id": i, "vector": vectors[i], "text": docs[i]}
    for i in range(len(vectors))
]

res = client.insert(collection_name="demo_collection", data=data)

print(res)

while True:
    query = input("Enter a query: ")
    query_vectors = encode_queries([query])
    res = client.search(
        collection_name="demo_collection",
        data=query_vectors,
        limit=2,
        output_fields=["text"],
    )
    for entity in res[0]:
        print(entity['entity']['text'])