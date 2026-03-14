import requests

# put your AI API key here
OPENAI_API_KEY = "PASTE_YOUR_API_KEY"

def explain_threat(threat_info):

    prompt = f"""
You are a cybersecurity SOC assistant.

Analyze the following threat and explain it in simple human readable form.

Threat Information:
{threat_info}

Provide:

1. What the threat is
2. Why it is dangerous
3. How it may affect the system
4. Step-by-step instructions to remove or mitigate it
5. Extra security recommendations

Keep the answer clear and practical.
"""

    url = "https://api.openai.com/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3
    }

    response = requests.post(url, headers=headers, json=data)

    result = response.json()

    return result["choices"][0]["message"]["content"]