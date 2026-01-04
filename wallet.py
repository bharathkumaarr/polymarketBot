import requests
import time
from config import BASE_URL

SECONDS_IN_DAY = 86400

def get_wallet_activity(address):
    url = f"{BASE_URL}/activity"
    params = {"user": address}
    r = requests.get(url, params=params, timeout=10)
    r.raise_for_status()
    data = r.json()

    total = len(data)
    polymarket_trades = sum(
        1 for a in data if a.get("type") == "TRADE"
    )

    if total == 0:
        age_days = 0
    else:
        oldest = min(a["timestamp"] for a in data)
        age_days = (time.time() - oldest) / SECONDS_IN_DAY

    return {
        "total_activity": total,
        "polymarket_trades": polymarket_trades,
        "age_days": age_days
    }
