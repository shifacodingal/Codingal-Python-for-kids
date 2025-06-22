actual_cost = float(input("Enter the actual cost of the product: "))
selling_price = float(input("Enter the selling price of the product: "))
if selling_price > actual_cost:
    profit = selling_price - actual_cost
    profit_percentage = (profit / actual_cost) * 100
    print(f"Profit: {profit:.2f}")
    print(f"Profit Percentage: {profit_percentage:.2f}%")