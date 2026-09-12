MAX_POSITION_SOL = 0.10
MAX_DAILY_LOSS_SOL = 0.50
STOP_LOSS_PCT = 0.12
TAKE_PROFIT_PCT = 0.25
MAX_OPEN_POSITIONS = 3

MIN_LIQUIDITY_USD = 25_000
MIN_VOLUME_5M_USD = 10_000
MAX_TOP10_HOLDER_PCT = 35
MIN_TOKEN_AGE_SECONDS = 60

def should_buy(token):
    if token.liquidity_usd < MIN_LIQUIDITY_USD:
        return False

    if token.volume_5m_usd < MIN_VOLUME_5M_USD:
        return False

    if token.top10_holder_pct > MAX_TOP10_HOLDER_PCT:
        return False

    if token.age_seconds < MIN_TOKEN_AGE_SECONDS:
        return False

    if daily_loss_sol() >= MAX_DAILY_LOSS_SOL:
        return False

    if open_positions() >= MAX_OPEN_POSITIONS:
        return False

    return calculate_score(token) >= 75

TRADING_MODE=testnet

if daily_loss_sol() >= MAX_DAILY_LOSS_SOL:
    trading_enabled = False
    alert("DAILY LOSS LIMIT REACHED")

