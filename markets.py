
import requests
from config import BASE_URL

def fetch_events(limit=50, offset=0):
    params = {
        "closed": "false",
        "order": "id",
        "ascending": "false",
        "limit": limit,
        "offset": offset
    }
    r = requests.get(f"{BASE_URL}/events", params=params, timeout=10)
    r.raise_for_status()
    return r.json()

def extract_markets(events):
    markets = []
    for event in events:
        for m in event.get("markets", []):
            markets.append(m)
    return markets
