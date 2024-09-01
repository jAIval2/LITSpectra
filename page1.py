import streamlit as st

# Set page configuration
st.set_page_config(page_title="Forecast Your Savings", layout="wide")

# Custom CSS for layout
st.markdown("""
    <style>
        body {
            background-color: #0d3a4e;
            color: #ffffff;
            font-family: 'Arial', sans-serif;
        }
        .container {
            display: flex;
            justify-content: space-between;
            padding: 20px;
            background-color: #0d3a4e;
            border-radius: 10px;
            gap: 20px;
        }
        .left-column {
            flex: 1;
            background-color: #0b2a39;
            padding: 20px;
            border-radius: 10px;
        }
        .header {
            font-size: 28px;
            font-weight: bold;
            color: #32E673;
            margin-bottom: 20px;
        }
        .sub-header {
            font-size: 24px;
            margin-bottom: 15px;
        }
        .button {
            background-color: #00D082;
            color: #ffffff;
            border: none;
            border-radius: 10px;
            padding: 10px 20px;
            cursor: pointer;
        }
        .metrics-container {
            display: flex;
            justify-content: space-between;
            margin-top: 20px;
        }
        .metric-box {
            flex: 1;
            text-align: center;
            padding: 10px;
            background-color: #0b2a39;
            border-radius: 10px;
            margin: 0 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Main Container
st.markdown("""
    <div class="container">
        <div class="left-column">
            <div class="header">Forecast Your Savings</div>
            <div class="sub-header">SoBo 590 <span style="background-color: #00D082; border-radius: 5px; padding: 3px 10px;">Operational Until 2039</span></div>
            <div>Every unit of electricity from this project is ₹5 discount per unit on your power bill</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# Input Fields and Sliders
avg_power_bill = st.number_input("Enter avg power bill", value=2500, min_value=0, step=100)
savings_range = st.slider("Choose savings range (%)", min_value=0, max_value=100, value=75)


# Function to calculate tiered electricity cost and units consumed
def calculate_units_from_amount(amount):
    if amount < 0:
        return 0

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


# Calculate the total units consumed from the average bill
total_units = calculate_units_from_amount(avg_power_bill)

# Calculate the percentage of total units user wants to save
units_to_save = total_units * savings_range / 100

# Convert units to annual kWh
annual_kwh = units_to_save * 12

# Calculate savings from solar credits (₹5 per unit)
monthly_savings_from_solar = units_to_save * 5
annual_savings_from_solar = monthly_savings_from_solar * 12
fifteen_year_savings = annual_savings_from_solar * 15

# Calculate the total cost of saved units
new_monthly_bill = avg_power_bill - monthly_savings_from_solar

# Calculate the monthly savings
monthly_savings = avg_power_bill - new_monthly_bill

# Calculate energy produced per month
energy_produced_per_month = annual_kwh / 12

# Display Metrics aligned horizontally
st.markdown("""
    <div class="metrics-container">
        <div class="metric-box">
            <h4>Units Consumed</h4>
            <p>{total_units:,.2f} units</p>
            <small>Approximate number of units consumed</small>
        </div>
        <div class="metric-box">
            <h4>Reserved Solar</h4>
            <p>{annual_kwh:,.2f} kWh</p>
            <small>Annual reserved solar based on your savings target</small>
        </div>
        <div class="metric-box">
            <h4>Energy Produced/Month</h4>
            <p>{energy_produced_per_month:,.2f} kWh</p>
            <small>Energy produced monthly from reserved solar</small>
        </div>
        <div class="metric-box">
            <h4>Monthly Savings</h4>
            <p>₹{monthly_savings:,.2f}</p>
            <small>Difference between original and new bill</small>
        </div>
        <div class="metric-box">
            <h4>Annual Savings</h4>
            <p>₹{annual_savings_from_solar:,.2f}</p>
            <small>Total savings per year</small>
        </div>
        <div class="metric-box">
            <h4>15-Year Savings</h4>
            <p>₹{fifteen_year_savings:,.2f}</p>
            <small>Total savings over 15 years</small>
        </div>
    </div>
""".format(
    total_units=total_units,
    annual_kwh=annual_kwh,
    energy_produced_per_month=energy_produced_per_month,
    monthly_savings=monthly_savings,
    annual_savings_from_solar=annual_savings_from_solar,
    fifteen_year_savings=fifteen_year_savings
), unsafe_allow_html=True)
