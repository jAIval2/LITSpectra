def calculate_units_from_amount(amount):
    if amount < 0:
        return "Invalid amount."

    units = 0

    # Tier 1: ₹4.71 per unit for the first 100 units
    tier1_rate = 4.71
    tier1_limit = 100
    tier1_cost = tier1_rate * tier1_limit

    if amount > tier1_cost:
        units += tier1_limit
        amount -= tier1_cost
    else:
        return amount / tier1_rate

    # Tier 2: ₹10.29 per unit for the next 200 units (101-300)
    tier2_rate = 10.29
    tier2_limit = 200
    tier2_cost = tier2_rate * tier2_limit

    if amount > tier2_cost:
        units += tier2_limit
        amount -= tier2_cost
    else:
        return units + (amount / tier2_rate)

    # Tier 3: ₹14.55 per unit for the next 200 units (301-500)
    tier3_rate = 14.55
    tier3_limit = 200
    tier3_cost = tier3_rate * tier3_limit

    if amount > tier3_cost:
        units += tier3_limit
        amount -= tier3_cost
    else:
        return units + (amount / tier3_rate)

    # Tier 4: ₹16.64 per unit for the next 500 units (501-1000)
    tier4_rate = 16.64
    tier4_limit = 500
    tier4_cost = tier4_rate * tier4_limit

    if amount > tier4_cost:
        units += tier4_limit
        amount -= tier4_cost
    else:
        return units + (amount / tier4_rate)

    # Tier 5: ₹16.64 per unit for units above 1000
    units += amount / tier4_rate
    return units


# Input the total amount paid
try:
    amount = float(input("Enter the total amount paid: ₹"))
    units = calculate_units_from_amount(amount)
    print(f"The approximate number of units consumed is: {units:.2f}")
except ValueError:
    print("Please enter a valid amount.")
