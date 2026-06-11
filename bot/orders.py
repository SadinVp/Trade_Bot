from bot.client import get_client
from bot.logging_config import logger


def place_market_order(symbol, side, quantity):
    """
    Place a MARKET order on Binance Futures Testnet.
    """
    client = get_client()

    try:
        logger.info(
            f"Placing MARKET order | Symbol={symbol}, Side={side}, Quantity={quantity}"
        )

        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity,
        )

        logger.info(f"MARKET order successful: {response}")
        return response

    except Exception as e:
        logger.error(f"MARKET order failed: {e}")
        raise


def place_limit_order(symbol, side, quantity, price):
    """
    Place a LIMIT order on Binance Futures Testnet.
    """
    client = get_client()

    try:
        logger.info(
            f"Placing LIMIT order | Symbol={symbol}, Side={side}, "
            f"Quantity={quantity}, Price={price}"
        )

        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC",  # Good Till Cancelled
        )

        logger.info(f"LIMIT order successful: {response}")
        return response

    except Exception as e:
        logger.error(f"LIMIT order failed: {e}")
        raise