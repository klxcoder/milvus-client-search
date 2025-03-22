import requests
import json

CHAT_MODEL = "llama3.2"

def chat(query, rag_data):
    messages = [{
        "role": "system",
        "content": (
            "Your name is klxcoder."
        )
    }]
    for line in rag_data:
        [question, answer] = line.split("?")
        messages.append({
            "role": "user",
            "content": question.strip() + "?"
        })
        messages.append({
            "role": "assistant",
            "content": answer.strip()
        })
    messages.append({
        "role": "user",
        "content": query
    })
    print(messages)
    with requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": CHAT_MODEL,
            "messages": messages,
            "stream": True,
        },
        stream=True  # Enable streaming
    ) as response:
        response.raise_for_status()  # Ensure request success
        for line in response.iter_lines():
            if line:
                data = json.loads(line)
                content = data.get("message", {}).get("content", "")
                print(content, end="", flush=True)

if __name__ == '__main__':
    rag_data = [
        "The Eiffel Tower is in Paris.",
        "It was built in 1889.",
        "Paris is the capital of France."
    ]
    chat("Where is the Eiffel Tower?", rag_data)
