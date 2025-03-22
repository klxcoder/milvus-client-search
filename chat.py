import requests
import json

CHAT_MODEL = "llama3.2"

def chat(query):
    with requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": CHAT_MODEL,
            "messages": [
                {
                    "role": "system",
                    "content": "Use this data: Eiffel Tower is in Paris. It was built in 1889."
                },
                {
                    "role": "user",
                    "content": query
                }
            ],
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
    chat("Where is the Eiffel Tower?")
