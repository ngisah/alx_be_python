monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your monthly expenses: "))
monthly_savings = float(monthly_income) - float(monthly_expenses)

# projected saving for one year assuming it gets 5% interest
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print(f"Your monthly savings are: {monthly_savings}")
print(f"Projected savings after one year, with interest, is: ${projected_savings}")