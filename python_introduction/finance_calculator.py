monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your monthly expenses: "))
savings = monthly_income - monthly_expenses

# projected saving for one year assuming it gets 5% interest
projected_saving = savings * 12 + (savings * 12 * 0.05)

print(f"Your monthly savings are: {savings}")
print(f"projected savings after one year, with interest, is: ${projected_saving}")