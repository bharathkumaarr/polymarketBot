import requests
from config import BASE_URL

def fetch_recent_trades(limit=50):
    """
    Returns latest trades across Polymarket
    """
    url = f"{BASE_URL}/trades"
    params = {
        "limit": limit
    }
    r = requests.get(url, params=params, timeout=10)
    r.raise_for_status()
    return r.json()
