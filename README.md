# Binance Futures Testnet Trading Bot

A simple Python CLI application that places **MARKET** and **LIMIT** orders on the **Binance Futures Testnet (USDT-M)**. The project is built with a modular structure and includes input validation, logging, and exception handling.

---

## Features

- ✅ Place **MARKET** orders
- ✅ Place **LIMIT** orders
- ✅ Supports both **BUY** and **SELL**
- ✅ Command Line Interface (CLI) using `argparse`
- ✅ Input validation
- ✅ Logs API requests, responses, and errors
- ✅ Exception handling for invalid inputs and API failures
- ✅ Uses Binance Futures Testnet (safe for testing)

---

## Project Structure

```
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
│   └── cli.py
│
├── logs/
│   └── trading_bot.log
│
├── .env
├── requirements.txt
├── README.md
└── test_connection.py
```

---

## Requirements

- Python 3.9+
- Binance Futures Testnet Account
- Testnet API Key and Secret

---

## Installation

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd trading_bot
```

### 2. Create a virtual environment

#### macOS/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Configure API Keys

Create a `.env` file in the project root:

```env
API_KEY=YOUR_TESTNET_API_KEY
API_SECRET=YOUR_TESTNET_API_SECRET
```

> **Important:** Use **Binance Futures Testnet** API keys, not production Binance API keys.

---

## Verify Connection

Run:

```bash
python test_connection.py
```

Expected output:

```
✅ Connection successful!
```

---

## Running the Trading Bot

### Place a MARKET BUY order

```bash
python -m bot.cli \
    --symbol BTCUSDT \
    --side BUY \
    --type MARKET \
    --quantity 0.001
```

### Place a MARKET SELL order

```bash
python -m bot.cli \
    --symbol BTCUSDT \
    --side SELL \
    --type MARKET \
    --quantity 0.001
```

### Place a LIMIT BUY order

```bash
python -m bot.cli \
    --symbol BTCUSDT \
    --side BUY \
    --type LIMIT \
    --quantity 0.001 \
    --price 50000
```

### Place a LIMIT SELL order

```bash
python -m bot.cli \
    --symbol BTCUSDT \
    --side SELL \
    --type LIMIT \
    --quantity 0.001 \
    --price 100000
```

---

## Sample Output

```
========== ORDER REQUEST ==========
Symbol   : BTCUSDT
Side     : BUY
Type     : MARKET
Quantity : 0.001
===================================

✅ ORDER PLACED SUCCESSFULLY

Order ID      : 123456789
Status        : FILLED
Executed Qty  : 0.001
Average Price : 107250.45
```

---

## Logging

All requests, responses, and errors are stored in:

```
logs/trading_bot.log
```

Example:

```
2026-06-11 20:15:30 - INFO - Placing MARKET order | Symbol=BTCUSDT, Side=BUY, Quantity=0.001
2026-06-11 20:15:31 - INFO - MARKET order successful: {...}
```

---

## Error Handling

The application validates:

- Trading symbol
- Order side (`BUY` or `SELL`)
- Order type (`MARKET` or `LIMIT`)
- Quantity must be greater than zero
- Price is required for `LIMIT` orders

API and network exceptions are caught and logged.

---

## Assumptions

- The application is intended for **Binance Futures Testnet** only.
- The user has valid Testnet API credentials.
- Supported order types are `MARKET` and `LIMIT`.
- Supported sides are `BUY` and `SELL`.
- The trading symbol exists on Binance Futures Testnet.

---

## Technologies Used

- Python 3
- python-binance
- python-dotenv
- argparse
- logging

---

## Future Enhancements

- Stop-Limit orders
- OCO orders
- Interactive CLI menus
- Web dashboard
- Order history
- Position monitoring