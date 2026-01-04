# main.py
import time
from markets import fetch_events, extract_markets
from detector import is_anomalous
from alert import send_alert
from config import POLL_INTERVAL
from datetime import datetime, timezone

ts = datetime.now(timezone.utc).strftime("%H:%M:%S UTC")



print("🚀 Polymarket Gamma bot started")

previous_volume = {}

while True:
    try:
        events = fetch_events(limit=50)
        markets = extract_markets(events)

        for m in markets:
            market_id = m["id"]

            # cast immediately
            volume = float(m.get("volume") or 0)
            liquidity = float(m.get("liquidity") or 0)

            # previous snapshot
            prev = previous_volume.get(market_id, volume)
            delta = volume - prev

            # trace log
            # print(
            #     f"[TRACE] {m.get('question')[:40]} | "
            #     f"vol={volume:.0f} prev={prev:.0f} Δ={delta:.0f}"
            # )

            # anomaly detection
            if is_anomalous(m, previous_volume):
                msg = (
                    f"🚨 *Unusual Market Activity*\n\n"
                    f"Market: {m.get('question')}\n"
                    f"Volume Spike: ${delta:,.0f}\n"
                    f"Total Volume: ${volume:,.0f}\n"
                    f"Liquidity: ${liquidity:,.0f}\n"
                    f"Time: {ts}\n"
                )
                send_alert(msg)

            # update snapshot LAST
            previous_volume[market_id] = volume




    except Exception as e:
        print("Error:", e)
        time.sleep(5)
