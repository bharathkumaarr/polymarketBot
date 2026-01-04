import requests

url = "https://data-api.polymarket.com/trades"
r = requests.get(url, params={"limit": 5}, timeout=10)
print(r.status_code)
print(r.json())
