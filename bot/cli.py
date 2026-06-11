import argparse

from bot.orders import place_market_order, place_limit_order
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
)


def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    # Define CLI arguments
    parser.add_argument(
        "--symbol",
        type=str,
        required=True,
        help="Trading symbol (e.g. BTCUSDT)",
    )

    parser.add_argument(
        "--side",
        type=str,
        required=True,
        help="BUY or SELL",
    )

    parser.add_argument(
        "--type",
        type=str,
        required=True,
        help="MARKET or LIMIT",
    )

    parser.add_argument(
        "--quantity",
        type=float,
        required=True,
        help="Order quantity",
    )

    parser.add_argument(
        "--price",
        type=float,
        help="Price (required only for LIMIT orders)",
    )

    args = parser.parse_args()

    try:
        # Validate inputs
        validate_symbol(args.symbol)
        validate_side(args.side)
        validate_order_type(args.type)
        validate_quantity(args.quantity)
        validate_price(args.type, args.price)

        print("\n========== ORDER REQUEST ==========")
        print(f"Symbol   : {args.symbol}")
        print(f"Side     : {args.side}")
        print(f"Type     : {args.type}")
        print(f"Quantity : {args.quantity}")

        if args.type.upper() == "LIMIT":
            print(f"Price    : {args.price}")

        print("===================================\n")

        # Place the order
        if args.type.upper() == "MARKET":
            response = place_market_order(
                symbol=args.symbol,
                side=args.side.upper(),
                quantity=args.quantity,
            )

        else:
            response = place_limit_order(
                symbol=args.symbol,
                side=args.side.upper(),
                quantity=args.quantity,
                price=args.price,
            )

        print("✅ ORDER PLACED SUCCESSFULLY\n")

        print("Order ID      :", response.get("orderId"))
        print("Status        :", response.get("status"))
        print("Executed Qty  :", response.get("executedQty"))
        print("Average Price :", response.get("avgPrice", "N/A"))

    except Exception as e:
        print("\n❌ ERROR")
        print(e)


if __name__ == "__main__":
    main()