import random

DIMENSION = 768

def encode_queries(queries):
    return [[random.uniform(-1, 1) for _ in range(DIMENSION)] for _ in queries]

if __name__ == '__main__':
    query_vectors = encode_queries(["Who is Alan Turing?"])
    print(query_vectors)
