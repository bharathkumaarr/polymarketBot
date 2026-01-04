# test_api.py
import requests

BASE_URL = "https://gamma-api.polymarket.com"

params = {
    "closed": "false",
    "order": "id",
    "ascending": "false",
    "limit": 5
}

r = requests.get(f"{BASE_URL}/events", params=params, timeout=10)
r.raise_for_status()

events = r.json()

print(f"[OK] status={r.status_code}")
print(f"[OK] events fetched={len(events)}")

# inspect structure
event = events[0]
markets = event.get("markets", [])

print(f"[OK] markets in first event={len(markets)}")

if markets:
    m = markets[0]

    # show raw values
    print("\n[RAW MARKET SAMPLE]")
    print("question:", m.get("question"))
    print("volume (raw):", m.get("volume"), type(m.get("volume")))
    print("liquidity (raw):", m.get("liquidity"), type(m.get("liquidity")))

    # safe numeric casting
    volume = float(m.get("volume") or 0)
    liquidity = float(m.get("liquidity") or 0)

    print("\n[CASTED VALUES]")
    print("volume (float):", volume)
    print("liquidity (float):", liquidity)
else:
    print("[WARN] no markets found in event")
