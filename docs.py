def read_docs_to_list(file_path: str) -> list[str]:
    with open(file_path, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file if line.strip()]

if __name__ == '__main__':
    docs = read_docs_to_list('docs.txt')
    print(docs)
