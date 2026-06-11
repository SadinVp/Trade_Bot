VALID_SIDES = ["BUY", "SELL"]
VALID_TYPES = ["MARKET", "LIMIT"]


def validate_symbol(symbol):
    if not symbol:
        raise ValueError("Symbol cannot be empty.")


def validate_side(side):
    if side.upper() not in VALID_SIDES:
        raise ValueError("Side must be BUY or SELL.")


def validate_order_type(order_type):
    if order_type.upper() not in VALID_TYPES:
        raise ValueError("Order type must be MARKET or LIMIT.")


def validate_quantity(quantity):
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")


def validate_price(order_type, price):
    if order_type.upper() == "LIMIT":
        if price is None:
            raise ValueError("Price is required for LIMIT orders.")
        if price <= 0:
            raise ValueError("Price must be greater than zero.")