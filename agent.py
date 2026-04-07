import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def run_agent(log):

    prompt = f"""
You are a DevOps expert.

Analyze this error:
{log}

Give:
1. Root cause
2. Fix
3. Command
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()

    return result["response"]