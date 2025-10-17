# Business Profit Calculator
# Calculates profit and margin percentage from revenue and cost data

# Get revenue from user
revenue = float(input("Enter total revenue: $"))

# Get costs from user
costs = float(input("Enter total costs: $"))

# Calculate profit
profit = revenue - costs  # use normal minus sign

# Calculate profit margin percentage
margin = (profit / revenue) * 100

# Display results
print("\n--- Financial Summary ---")
print(f"Revenue: ${revenue:,.2f}")
print(f"Costs: ${costs:,.2f}")
print(f"Profit: ${profit:,.2f}")
print(f"Profit Margin: {margin:.1f}%")

# Add comment based on profit
if profit > 8000:
    comment = "Elon Musk who?"
elif profit > 5000:
    comment = "You rock"
elif profit > 3000:
    comment = "Excellent"
elif profit > 2000:
    comment = "Average"
elif profit > 1000:
    comment = "Good"
else:
    comment = "Keep trying"

print(f"Comment: {comment}")
