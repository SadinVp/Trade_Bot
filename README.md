# Binance Futures Testnet Trading Bot

## Overview

This project is a Python-based trading bot that interacts with the **Binance Futures Testnet (USDT-M)**. It allows users to place **MARKET** and **LIMIT** orders for both **BUY** and **SELL** operations through a command-line interface.

The application follows a modular design with separate components for API communication, order processing, validation, and logging. It also includes an enhanced interactive CLI that guides users through order placement.

---

# Features

* Place **MARKET** orders
* Place **LIMIT** orders
* Supports both **BUY** and **SELL**
* Interactive CLI menu (Bonus Feature)
* Command-line argument support
* Input validation
* Exception handling
* API request and response logging
* Binance Futures Testnet integration

---

# Project Structure

```
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── cli.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
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

# Setup Steps

## 1. Clone the repository

```bash
git clone <repository-url>
cd trading_bot
```

## 2. Create and activate a virtual environment

### macOS/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Configure API credentials

Create a `.env` file in the project root:

```env
API_KEY=YOUR_BINANCE_TESTNET_API_KEY
API_SECRET=YOUR_BINANCE_TESTNET_API_SECRET
```

## 5. Verify the connection

```bash
python test_connection.py
```

If successful, the application should connect to the Binance Futures Testnet without errors.

---

# How to Run

## Option 1: Interactive Mode (Recommended)

Run:

```bash
python -m bot.cli
```

The application will prompt for:

* Order Type (MARKET or LIMIT)
* Symbol
* Side (BUY or SELL)
* Quantity
* Price (for LIMIT orders)

Example:

```
===================================
 Binance Futures Testnet Trading Bot
===================================

Select Order Type
1. MARKET
2. LIMIT

Enter your choice (1/2): 1
Enter Symbol (e.g. BTCUSDT): BTCUSDT
Enter Side (BUY/SELL): BUY
Enter Quantity: 0.001
```

---

## Option 2: Command-Line Arguments

### MARKET Order

```bash
python -m bot.cli \
  --symbol BTCUSDT \
  --side BUY \
  --type MARKET \
  --quantity 0.001
```

### LIMIT Order

```bash
python -m bot.cli \
  --symbol BTCUSDT \
  --side SELL \
  --type LIMIT \
  --quantity 0.001 \
  --price 150000
```

---

# Logging

Application logs are stored in:

```
logs/trading_bot.log
```

The log file records:

* Order requests
* Successful API responses
* Errors and exceptions

---

# Assumptions

* The application is intended for **Binance Futures Testnet (USDT-M)** only.
* Users must generate valid **Testnet API credentials** before running the application.
* Supported order types are **MARKET** and **LIMIT**.
* Supported order sides are **BUY** and **SELL**.
* The trading symbol must exist on Binance Futures Testnet.
* Internet connectivity is required for communication with Binance APIs.

---

# Technologies Used

* Python 3
* python-binance
* python-dotenv
* argparse
* logging

---

# Bonus Feature Implemented

**Enhanced CLI UX**

The application provides an interactive menu-driven interface that guides users through order placement with prompts and validation messages, improving usability compared to requiring long command-line arguments.
