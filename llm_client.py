import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen2.5"


def call_llm(prompt: str) -> str:
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False,
            },
            timeout=60,
        )
        response.raise_for_status()
    except requests.RequestException as exc:
        raise RuntimeError(
            "Failed to reach Ollama at http://localhost:11434/api/generate. "
            "Make sure Ollama is running and the qwen2.5 model is available."
        ) from exc

    return response.json()["response"]
