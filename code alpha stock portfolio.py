import random

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, symbol, quantity, buy_price):
        """Add stock to the portfolio"""
        symbol = symbol.upper()
        if symbol in self.portfolio:
            self.portfolio[symbol]['quantity'] += quantity
            self.portfolio[symbol]['buy_price'] = (
                (self.portfolio[symbol]['buy_price'] * self.portfolio[symbol]['quantity']) + (buy_price * quantity)
            ) / (self.portfolio[symbol]['quantity'] + quantity)
        else:
            self.portfolio[symbol] = {"quantity": quantity, "buy_price": buy_price}

    def remove_stock(self, symbol):
        """Remove stock from the portfolio"""
        symbol = symbol.upper()
        if symbol in self.portfolio:
            del self.portfolio[symbol]
            print(f"{symbol} removed from portfolio.")
        else:
            print(f"{symbol} not found in portfolio.")

    def fetch_live_price(self, symbol):
        """Fetch the live price of a stock using Yahoo Finance"""
        try:
            stock = yf.Ticker(symbol)
            return stock.history(period="1d")["Close"].iloc[-1]
        except Exception as e:
            print(f"Error fetching data for {symbol}: {e}")
            return None

    def view_portfolio(self):
        """Display portfolio details with live prices"""
        if not self.portfolio:
            print("\nYour portfolio is empty!")
            return

        total_invested = 0
        total_value = 0

        print("\nStock Portfolio Summary:")
        print("-" * 60)
        print(f"{'Stock':<10}{'Qty':<10}{'Buy Price':<12}{'Live Price':<12}{'P/L'}")
        print("-" * 60)

        for symbol, details in self.portfolio.items():
            live_price = self.fetch_live_price(symbol)
            if live_price:
                quantity = details["quantity"]
                invested = quantity * details["buy_price"]
                current_value = quantity * live_price
                profit_loss = current_value - invested

                total_invested += invested
                total_value += current_value

                print(f"{symbol:<10}{quantity:<10}{details['buy_price']:<12.2f}{live_price:<12.2f}{profit_loss:.2f}")

        print("-" * 60)
        print(f"Total Invested: ${total_invested:.2f}")
        print(f"Current Portfolio Value: ${total_value:.2f}")
        print(f"Overall P/L: ${total_value - total_invested:.2f}")
        print("-" * 60)

# Interactive CLI
def main():
    portfolio = StockPortfolio()

    while True:
        print("\nStock Portfolio Tracker")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            symbol = input("Enter stock symbol (e.g., AAPL, TSLA): ").upper()
            quantity = int(input("Enter quantity: "))
            buy_price = float(input("Enter purchase price: "))
            portfolio.add_stock(symbol, quantity, buy_price)
            print(f"{symbol} added to portfolio.")

        elif choice == "2":
            symbol = input("Enter stock symbol to remove: ").upper()
            portfolio.remove_stock(symbol)

        elif choice == "3":
            portfolio.view_portfolio()

        elif choice == "4":
            print("Exiting Stock Portfolio Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()