# detector.py

def to_float(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return 0.0


def is_anomalous(market, previous_snapshot):
    market_id = market["id"]

    volume = to_float(market.get("volume"))
    liquidity = to_float(market.get("liquidity"))

    if liquidity <= 0:
        return False

    prev_volume = to_float(previous_snapshot.get(market_id))
    delta = volume - prev_volume

    if delta >= 10_000 and liquidity >= 25_000:
        return True

    return False
