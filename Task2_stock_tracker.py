# Task 2: Stock Portfolio Tracker
# CodeAlpha Python Programming Internship
# Author: Aryan Pandey

def stock_portfolio_tracker():
    """
    Simple stock tracker that calculates total investment based on manually defined stock prices.
    """
    # Hardcoded dictionary of stock prices
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 140,
        "MSFT": 380,
        "AMZN": 180,
        "META": 500,
        "NVDA": 880,
        "NFLX": 630
    }
    
    print("=" * 60)
    print("Stock Portfolio Tracker")
    print("=" * 60)
    print("\nAvailable stocks and their prices:")
    for stock, price in stock_prices.items():
        print(f"  {stock}: ${price}")
    
    print("\nEnter your stock portfolio:")
    print("(Enter 'done' when finished)\n")
    
    portfolio = {}
    total_investment = 0
    
    while True:
        stock_symbol = input("Enter stock symbol (or 'done'): ").upper().strip()
        
        if stock_symbol == 'DONE':
            break
        
        if stock_symbol not in stock_prices:
            print(f"Stock '{stock_symbol}' not found. Available stocks: {', '.join(stock_prices.keys())}")
            continue
        
        try:
            quantity = int(input(f"Enter quantity for {stock_symbol}: "))
            if quantity <= 0:
                print("Quantity must be a positive number.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        # Calculate investment for this stock
        investment = stock_prices[stock_symbol] * quantity
        portfolio[stock_symbol] = {
            "price": stock_prices[stock_symbol],
            "quantity": quantity,
            "investment": investment
        }
        total_investment += investment
        print(f"Added {quantity} shares of {stock_symbol} at ${stock_prices[stock_symbol]} each (${investment})")
    
    # Display portfolio summary
    print("\n" + "=" * 60)
    print("PORTFOLIO SUMMARY")
    print("=" * 60)
    
    if not portfolio:
        print("No stocks in portfolio.")
        return
    
    print(f"{'Stock':<10} {'Price':<10} {'Quantity':<10} {'Investment':<15}")
    print("-" * 60)
    
    for stock, data in portfolio.items():
        print(f"{stock:<10} ${data['price']:<9} {data['quantity']:<10} ${data['investment']:<14,.2f}")
    
    print("-" * 60)
    print(f"{'TOTAL INVESTMENT:':<30} ${total_investment:,.2f}")
    
    # Option to save to file
    save_option = input("\nDo you want to save this report to a file? (y/n): ").lower().strip()
    
    if save_option == 'y':
        filename = input("Enter filename (without extension): ").strip()
        if not filename:
            filename = "portfolio_report"
        
        # Save to .txt file
        with open(f"{filename}.txt", "w") as f:
            f.write("STOCK PORTFOLIO REPORT\n")
            f.write("=" * 60 + "\n")
            f.write(f"Generated from Stock Portfolio Tracker\n\n")
            f.write(f"{'Stock':<10} {'Price':<10} {'Quantity':<10} {'Investment':<15}\n")
            f.write("-" * 60 + "\n")
            
            for stock, data in portfolio.items():
                f.write(f"{stock:<10} ${data['price']:<9} {data['quantity']:<10} ${data['investment']:<14,.2f}\n")
            
            f.write("-" * 60 + "\n")
            f.write(f"{'TOTAL INVESTMENT:':<30} ${total_investment:,.2f}\n")
        
        print(f"Report saved to {filename}.txt")

def main():
    """Main function to run the stock portfolio tracker."""
    stock_portfolio_tracker()
    print("\nThank you for using Stock Portfolio Tracker!")

if __name__ == "__main__":
    main()