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

query = input("Enter a query: ")
print(query.upper())
