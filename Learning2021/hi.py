def solve(meal_cost, tip_percent, tax_percent):
    # Write your code here
    tip = ((tip_percent / 100 ) * meal_cost)
    tax = ((tax_percent / 100 ) * meal_cost)
    total = meal_cost + tip + tax
    return round(total)


meal_cost = 12.00

tip_percent = 20

tax_percent = 8

print(solve(meal_cost, tip_percent, tax_percent))
