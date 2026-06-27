import requests

url = "https://api.frankfurter.app/latest"

def get_rates():
    response = requests.get(url, params={"from": "USD"}, timeout=10)
    
    
    if response.status_code != 200:
        return {}
    
    data = response.json()
    return data.get("rates", {})
