# Step 1: Predefined stock prices (making dictionary)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "AMZN": 130
}

portfolio = {}
total_investment = 0

print("Stock Portfolio Tracker")
print("Available stocks:", ", ".join(stock_prices.keys()))

# Step 2: Take user input
while True:
    stock = input("\nEnter stock name (or type 'done' to finish): ").upper()
    
    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available!")
        continue

    try:
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    portfolio[stock] = portfolio.get(stock, 0) + quantity

# Step 3: Calculate total investment
print("\n--- Portfolio Summary ---")

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity
    total_investment += investment

    print(f"{stock} -> {quantity} x {price} = {investment}")

print(f"\nTotal Investment = {total_investment}")

# Step 4: Save to file
with open("portfolio.txt", "w", encoding="utf-8") as file:
    file.write("Stock Portfolio Summary\n")
    file.write("-----------------------\n")

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        investment = price * quantity
        file.write(f"{stock} -> {quantity} x {price} = {investment}\n")

    file.write(f"\nTotal Investment = {total_investment}")

print("Portfolio saved to portfolio.txt")