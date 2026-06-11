import argparse

from bot.orders import place_market_order, place_limit_order
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
)


def place_order(symbol, side, order_type, quantity, price=None):
    # Validate inputs
    validate_symbol(symbol)
    validate_side(side)
    validate_order_type(order_type)
    validate_quantity(quantity)
    validate_price(order_type, price)

    print("\n========== ORDER REQUEST ==========")
    print(f"Symbol   : {symbol}")
    print(f"Side     : {side}")
    print(f"Type     : {order_type}")
    print(f"Quantity : {quantity}")

    if order_type == "LIMIT":
        print(f"Price    : {price}")

    print("===================================")

    # Place order
    if order_type == "MARKET":
        response = place_market_order(
            symbol=symbol,
            side=side,
            quantity=quantity,
        )
    else:
        response = place_limit_order(
            symbol=symbol,
            side=side,
            quantity=quantity,
            price=price,
        )

    print("\n✅ ORDER PLACED SUCCESSFULLY")

    print("\n========== ORDER RESPONSE ==========")
    print(f"Order ID        : {response.get('orderId')}")
    print(f"Status          : {response.get('status')}")
    print(f"Symbol          : {response.get('symbol')}")
    print(f"Side            : {response.get('side')}")
    print(f"Executed Qty    : {response.get('executedQty')}")
    print(f"Client Order ID : {response.get('clientOrderId')}")
    print("====================================")


def interactive_mode():
    print("\n===================================")
    print(" Binance Futures Testnet Trading Bot")
    print("===================================\n")

    print("Select Order Type")
    print("1. MARKET")
    print("2. LIMIT")

    choice = input("\nEnter your choice (1/2): ").strip()

    if choice == "1":
        order_type = "MARKET"
    elif choice == "2":
        order_type = "LIMIT"
    else:
        print("❌ Invalid choice.")
        return

    symbol = input("Enter Symbol (e.g. BTCUSDT): ").strip().upper()
    side = input("Enter Side (BUY/SELL): ").strip().upper()
    quantity = float(input("Enter Quantity: ").strip())

    price = None
    if order_type == "LIMIT":
        price = float(input("Enter Limit Price: ").strip())

    try:
        place_order(symbol, side, order_type, quantity, price)
    except Exception as e:
        print(f"\n❌ ERROR: {e}")


def cli_mode():
    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument("--symbol")
    parser.add_argument("--side")
    parser.add_argument("--type")
    parser.add_argument("--quantity", type=float)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    # If required arguments are missing, switch to interactive mode
    if (
        args.symbol is None
        or args.side is None
        or args.type is None
        or args.quantity is None
    ):
        interactive_mode()
        return

    try:
        place_order(
            symbol=args.symbol.upper(),
            side=args.side.upper(),
            order_type=args.type.upper(),
            quantity=args.quantity,
            price=args.price,
        )
    except Exception as e:
        print(f"\n❌ ERROR: {e}")


if __name__ == "__main__":
    cli_mode()