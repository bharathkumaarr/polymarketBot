# config.py

# ======================
# Polling
# ======================
POLL_INTERVAL = 10  # seconds

# ======================
# Anomaly thresholds (market-based)
# ======================
MIN_VOLUME_SPIKE_USDC = 50_000     # alert if volume jumps by this much
MIN_LIQUIDITY_USDC = 10_000        # ignore illiquid markets

# ======================
# Polymarket Gamma API
# ======================
BASE_URL = "https://gamma-api.polymarket.com"

# ======================
# Telegram
# ======================
TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
TELEGRAM_CHAT_ID = "YOUR_TELEGRAM_CHAT_ID"