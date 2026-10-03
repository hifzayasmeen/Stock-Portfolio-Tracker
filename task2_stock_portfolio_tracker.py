"""
CodeAlpha - Python Programming Internship
Task 2: Stock Portfolio Tracker
--------------------------------
A simple stock tracker that calculates total investment based on
manually defined (hardcoded) stock prices.

Key Concepts Used: dictionary, input/output, basic arithmetic,
file handling (optional saving to .txt/.csv).
"""

import csv
import os

# Hardcoded dictionary of stock prices (price per share, in USD)
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 145,
    "MSFT": 330,
    "META": 300,
    "NFLX": 420,
}


def show_available_stocks():
    print("\nAvailable stocks and prices (per share):")
    print("-" * 35)
    for symbol, price in STOCK_PRICES.items():
        print(f"{symbol:<8} ${price}")
    print("-" * 35)


def get_portfolio_input():
    """Collect stock names and quantities from the user."""
    portfolio = {}

    print("\nEnter the stocks you own. Type 'done' when finished.")
    while True:
        symbol = input("\nEnter stock symbol (or 'done' to finish): ").upper().strip()

        if symbol == "DONE":
            break

        if symbol not in STOCK_PRICES:
            print(f"'{symbol}' is not in our price list. Please choose from the list above.")
            continue

        while True:
            qty_input = input(f"Enter quantity of {symbol} shares: ").strip()
            if qty_input.isdigit() and int(qty_input) > 0:
                quantity = int(qty_input)
                break
            print("Please enter a valid positive whole number.")

        # If the stock is entered again, add to the existing quantity
        portfolio[symbol] = portfolio.get(symbol, 0) + quantity

    return portfolio


def calculate_portfolio_value(portfolio):
    """Calculate total investment value and a breakdown per stock."""
    breakdown = []
    total_value = 0

    for symbol, quantity in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * quantity
        total_value += value
        breakdown.append((symbol, quantity, price, value))

    return breakdown, total_value


def display_summary(breakdown, total_value):
    print("\n" + "=" * 50)
    print("PORTFOLIO SUMMARY")
    print("=" * 50)
    print(f"{'Symbol':<8}{'Qty':<8}{'Price':<10}{'Value':<10}")
    print("-" * 50)
    for symbol, quantity, price, value in breakdown:
        print(f"{symbol:<8}{quantity:<8}${price:<9}${value:<9}")
    print("-" * 50)
    print(f"TOTAL INVESTMENT VALUE: ${total_value:,.2f}")
    print("=" * 50)


def save_to_file(breakdown, total_value):
    """Optionally save the results to a .txt or .csv file."""
    choice = input("\nSave results to a file? (y/n): ").lower().strip()
    if choice != "y":
        return

    file_format = input("Choose format - txt or csv: ").lower().strip()
    output_dir = "portfolio_reports"
    os.makedirs(output_dir, exist_ok=True)

    if file_format == "csv":
        filepath = os.path.join(output_dir, "portfolio_summary.csv")
        with open(filepath, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Symbol", "Quantity", "Price Per Share", "Total Value"])
            for symbol, quantity, price, value in breakdown:
                writer.writerow([symbol, quantity, price, value])
            writer.writerow([])
            writer.writerow(["TOTAL INVESTMENT VALUE", "", "", total_value])
        print(f"Saved to {filepath}")

    else:
        filepath = os.path.join(output_dir, "portfolio_summary.txt")
        with open(filepath, "w") as f:
            f.write("PORTFOLIO SUMMARY\n")
            f.write("=" * 50 + "\n")
            f.write(f"{'Symbol':<8}{'Qty':<8}{'Price':<10}{'Value':<10}\n")
            f.write("-" * 50 + "\n")
            for symbol, quantity, price, value in breakdown:
                f.write(f"{symbol:<8}{quantity:<8}${price:<9}${value:<9}\n")
            f.write("-" * 50 + "\n")
            f.write(f"TOTAL INVESTMENT VALUE: ${total_value:,.2f}\n")
        print(f"Saved to {filepath}")


def main():
    print("=" * 50)
    print("STOCK PORTFOLIO TRACKER")
    print("=" * 50)

    show_available_stocks()
    portfolio = get_portfolio_input()

    if not portfolio:
        print("\nNo stocks entered. Exiting.")
        return

    breakdown, total_value = calculate_portfolio_value(portfolio)
    display_summary(breakdown, total_value)
    save_to_file(breakdown, total_value)


if __name__ == "__main__":
    main()
