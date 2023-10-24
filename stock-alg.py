import time
import yfinance as yf

def trading_algorithm(user_set_price, current_price, high_point):
    if current_price < user_set_price:
        buy_stock(current_price)
    else:
        if current_price > high_point:
            high_point = current_price
        elif current_price < high_point:
            sell_stock(current_price)

    return high_point

def buy_stock(price):
    print(f"Buying stock at price {price:.2f}")

def sell_stock(price):
    print(f"Selling stock at price {price:.2f}")

# Example usage of the trading algorithm
user_set_price = 1000   # User's initial investment
high_point = 0          # Initial high point

# Function to get live stock price using Yahoo Finance API
def get_live_stock_price(ticker):
    stock_data = yf.download(ticker, period="1s")  # Fetch data for the last 1 second
    if len(stock_data) > 0:
        return stock_data.iloc[-1]["Open"]
    return None

# Simulate 10 seconds of trading
for _ in range(10):
    current_price = get_live_stock_price("BTC-USD")
    if current_price is not None:
        high_point = trading_algorithm(user_set_price, current_price, high_point)
    else:
        print("Failed to fetch stock price.")
    time.sleep(1)

print(f"Final high point: {high_point:.2f}")