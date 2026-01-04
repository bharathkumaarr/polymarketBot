import time
from trades import fetch_recent_trades
from wallet import get_wallet_activity
from detector import is_anomalous
from alert import send_alert

seen = set()

print("🚀 Polymarket REST bot started")

while True:
    try:
        trades = fetch_recent_trades()

        for t in trades:
            trade_id = t.get("id")
            if trade_id in seen:
                continue
            seen.add(trade_id)

            wallet = t.get("taker") or t.get("maker")
            if not wallet:
                continue

            wallet_stats = get_wallet_activity(wallet)

            if is_anomalous(t, wallet_stats):
                msg = (
                    f"🚨 *Unusual Polymarket Bet*\n\n"
                    f"Market: {t.get('market_slug')}\n"
                    f"Outcome: {t.get('outcome')}\n"
                    f"Size: ${t.get('size_usdc'):,.0f}\n\n"
                    f"Wallet: `{wallet}`\n"
                    f"Wallet Age: {wallet_stats['age_days']:.1f} days\n"
                    f"Polymarket Trades: {wallet_stats['polymarket_trades']}\n"
                    f"Total Activity: {wallet_stats['total_activity']}"
                )
                send_alert(msg)

        time.sleep(10)

    except Exception as e:
        print("Error:", e)
        time.sleep(5)
