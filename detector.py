from config import (
    MIN_USDC_BET,
    MAX_WALLET_TRADES,
    MAX_TOTAL_ACTIVITY,
    MAX_WALLET_AGE_DAYS
)

def is_anomalous(trade, wallet):
    size = trade.get("size_usdc", 0)

    return (
        size >= MIN_USDC_BET and
        wallet["polymarket_trades"] <= MAX_WALLET_TRADES and
        wallet["total_activity"] <= MAX_TOTAL_ACTIVITY and
        wallet["age_days"] <= MAX_WALLET_AGE_DAYS
    )
