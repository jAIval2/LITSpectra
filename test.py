import streamlit as st
import base64

# Convert the image to Base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Paths to your images
background_image_path = r'C:\Users\sonal\PycharmProjects\LITSpectra\Designer.jpeg'
step1_image_path = r'C:\Users\sonal\PycharmProjects\LITSpectra\a.jpeg'
step2_image_path = r'C:\Users\sonal\PycharmProjects\LITSpectra\b.jpeg'
step3_image_path = r'C:\Users\sonal\PycharmProjects\LITSpectra\c.jpeg'

background_base64_image = get_base64_image(background_image_path)
step1_base64_image = get_base64_image(step1_image_path)
step2_base64_image = get_base64_image(step2_image_path)
step3_base64_image = get_base64_image(step3_image_path)

# Set page configuration
st.set_page_config(page_title="Solar over the Internet", layout="wide")

# Custom CSS for the team name, background image, and text overlay
st.markdown(f"""
    <style>
        .team-name {{
            position: fixed;
            top: 20px;
            left: 20px;
            font-size: 32px;
            font-weight: bold;
            color: #333;
            z-index: 10;
        }}
        .background-container {{
            position: relative;
            height: 100vh;
            background: url(data:image/png;base64,{background_base64_image}) no-repeat center center fixed;
            background-size: cover;
            color: #fff;
            text-align: center;
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            background-color: #fff;
        }}
        .centered-text {{
            font-size: 48px;
            font-weight: bold;
        }}
        .sub-text {{
            font-size: 24px;
            margin-top: 10px;
            font-weight: normal;
        }}
        .button-play {{
            margin-top: 20px;
            background-color: #60af32;
            color: #fff;
            border: none;
            border-radius: 10px;
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
        }}
        .features {{
            display: flex;
            justify-content: space-around;
            margin-top: 50px;
        }}
        .feature-box {{
            text-align: center;
            background-color:#32E673;
            color: #333;
            border-radius: 10px;
            padding: 20px;
            width: 30%;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }}
        .feature-box h3 {{
            font-size: 20px;
            margin-bottom: 10px;
        }}
        .feature-box p {{
            font-size: 16px;
            margin-bottom: 5px;
        }}
    </style>
""", unsafe_allow_html=True)

# Display the team name outside the background image
st.markdown('<div class="team-name">LIT Spectra</div>', unsafe_allow_html=True)

# Background and text overlay
st.markdown("""
    <div class="background-container">
        <div class="centered-text">
            Solar over the internet
            <div class="sub-text">Save up on power bills with Digital Solar</div>
            <button class="button-play">Introducing Digital Solar (1 min)</button>
        </div>
    </div>
""", unsafe_allow_html=True)

# Features Section
st.markdown("""
    <div class="features">
        <div class="feature-box">
            <h3>Needs no installation</h3>
            <p>No obtrusive structures on roof</p>
        </div>
        <div class="feature-box">
            <h3>Go solar instantly</h3>
            <p>3 mins, not the usual 3 months</p>
        </div>
        <div class="feature-box">
            <h3>Maximise Savings</h3>
            <p>Offsets at tax-free 11.5% XIRR</p>
        </div>
    </div>
""", unsafe_allow_html=True)

# Custom CSS for layout and styling
st.markdown(f"""
    <style>
        .step-container {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 50px;
        }}
        .step-text {{
            width: 45%;
        }}
        .step-image {{
            width: 45%;
            text-align: center;
        }}
        .step-title {{
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 10px;
        }}
        .step-description {{
            font-size: 18px;
            margin-bottom: 10px;
        }}
        .step-info {{
            background-color: #60af32;
            padding: 10px;
            border-radius: 10px;
            display: inline-block;
            font-size: 16px;
            margin-top: 10px;
        }}
        .step-image img {{
            max-width: 100%;
            border-radius: 10px;
        }}
        .step-number {{
            font-size: 20px;
            font-weight: bold;
            color: #6c757d;
            margin-bottom: 20px;
        }}
    </style>
""", unsafe_allow_html=True)

# Step 1
st.markdown(f"""
    <div class="step-container">
        <div class="step-text">
            <div class="step-number">Step 1</div>
            <div class="step-title">Enroll in a Solar Initiative</div>
            <div class="step-description">Join a solar initiative with LITSpectra by reserving the amount of solar energy needed to match your monthly electricity usage from one of the active projects. You'll earn credits for the energy generated by your reserved solar panels, directly reducing your electricity bill.
            <div class="step-description">Each credit earned equates to 1 Unit off your bill, making solar energy both affordable and beneficial.</div>
            <div class="step-info">1 credit = ₹1 offset on power bill</div>
        </div>
        <div class="step-image">
            <img src="data:image/png;base64,{step1_base64_image}" alt="Step 1 Image">
        </div>
    </div>
""", unsafe_allow_html=True)

# Step 2 (Reverse order: image on the left, text on the right)
st.markdown(f"""
    <div class="step-container" style="flex-direction: row-reverse;">
        <div class="step-text">
            <div class="step-number">Step 2</div>
            <div class="step-title">Connect Your Power Provider</div>
            <div class="step-description">Link your discom to your account, where your earned credits will be tracked and stored daily. By adding your billing details, you can easily apply these digital solar credits to your electricity bill. With over 70 utility providers across India supported by the platform, you can seamlessly integrate your solar savings with your existing power service.</div>
            <div class="step-info">Real-time savings tracking</div>
        </div>
        <div class="step-image">
            <img src="data:image/png;base64,{step2_base64_image}" alt="Step 2 Image">
        </div>
    </div>
""", unsafe_allow_html=True)

# Step 3
st.markdown(f"""
    <div class="step-container">
        <div class="step-text">
            <div class="step-number">Step 3</div>
            <div class="step-title">Offset Bills Using Credits</div>
            <div class="step-description">When it’s time to pay your electricity bill, simply use your account to apply the stored credits. You have the flexibility to fully offset your bill using these credits, potentially paying nothing at all. If your electricity usage exceeds the credits available, you can cover the remaining balance with your preferred payment method, ensuring a convenient and cost-effective way to manage your power expenses.</div>
            <div class="step-info">Automatic bill offset</div>
        </div>
        <div class="step-image">
            <img src="data:image/png;base64,{step3_base64_image}" alt="Step 3 Image">
        </div>
    </div>
""", unsafe_allow_html=True)

# Set page configuration

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
st.divider()
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
st.divider()
# Custom CSS for footer styling
st.markdown("""
    <style>
    .footer {
        color: white;
        padding: 20px;
        text-align: left;
        bottom: 0;
        width: 100%;
    }
    .footer-container {
        display: flex;
        justify-content: space-between;
    }
    .footer-column {
        margin-right: 30px;
    }
    .footer a {
        color: white;
        text-decoration: none;
        margin: 5px 0;
        display: block;
    }
    .footer a:hover {
        text-decoration: underline;
    }
    .social-icons img {
        width: 24px;
        margin-right: 10px;
    }
    </style>
    <div class="footer">
        <div class="footer-container">
            <div class="footer-column">
                <h4>LITSpectra</h4>
                <p>LITSpectra is a Digital Solar Platform that enables users to reserve solar from community solar projects to offset their power bills.</p>
                <div class="social-icons">
                    <a href="#"><img src="https://img.icons8.com/ios-filled/50/ffffff/linkedin.png"/></a>
                    <a href="#"><img src="https://img.icons8.com/ios-filled/50/ffffff/twitter.png"/></a>
                    <a href="#"><img src="https://img.icons8.com/ios-filled/50/ffffff/discord.png"/></a>
                    <a href="#"><img src="https://img.icons8.com/ios-filled/50/ffffff/instagram-new.png"/></a>
                </div>
            </div>
            <div class="footer-column">
                <h3>Digital Solar</h3>
                <a href="#">Community Solar Projects</a>
                <a href="#">How it Works</a>
                <a href="#">What's New</a>
                <a href="#">Refund Policy</a>
                <a href="#">EV Charging</a>
            </div>
            <div class="footer-column">
                <h3>Company</h3>
                <a href="#">About Us</a>
                <a href="#">Careers</a>
                <a href="#">Newsroom</a>
            </div>
            <div class="footer-column">
                <h3>Help</h3>
                <a href="#">Write to Us</a>
                <a href="#">Help Center</a>
            </div>
        </div>
        <div style="margin-top: 20px;">
            <p>© LITSpectra, 2024. All rights reserved.</p>
            <a href="#">Terms of Service</a> | <a href="#">Privacy Policy</a>
        </div>
    </div>
    """, unsafe_allow_html=True)
