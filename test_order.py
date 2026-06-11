from bot.orders import place_market_order

response = place_market_order(
    symbol="BTCUSDT",
    side="BUY",
    quantity=0.001,
)

print(response)