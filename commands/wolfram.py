import requests
from utils.api_usage import can_use_api
from utils.speak import speak

WOLFRAM_APP_ID = 'API KEY HERE'

def answer_wolfram(query):
    if not can_use_api():
        return None
    url = "http://api.wolframalpha.com/v2/query"
    params = {
        "input": query,
        "appid": WOLFRAM_APP_ID,
        "format": "plaintext",
        "output": "JSON"
    }
    try:
        response = requests.get(url, params=params)
        data = response.json()
        pods = data["queryresult"].get("pods", [])
        for pod in pods:
            if pod.get("title", "").lower() in ["result", "exact result"]:
                return pod["subpods"][0]["plaintext"]
        return None
    except Exception as e:
        print("Wolfram error:", e)
        return None
