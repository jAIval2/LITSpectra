import streamlit as st
import base64

# Convert the image to Base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Path to your image
image_path = r'C:\Users\sonal\PycharmProjects\LITSpectra\poa.png'
base64_image = get_base64_image(image_path)

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
            background: url(data:image/png;base64,{base64_image}) no-repeat center center fixed;
            background-size: cover;
            color: #fff;
            text-align: center;
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
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
            background-color: #333;
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
            background-color: #f0f0f0;
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

# Convert the image to Base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Path to your image
image_path = r'C:\Users\sonal\PycharmProjects\LITSpectra\a.png'
base64_image = get_base64_image(image_path)



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
            background-color: #e0f7f5;
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
st.markdown("""
    <div class="step-container">
        <div class="step-text">
            <div class="step-number">Step 1</div>
            <div class="step-title">Join a solar project</div>
            <div class="step-description">Reserve solar you need to offset your monthly power bill from an active project.
            You get credits for the power produced from your reserved solar panels.</div>
            <div class="step-info">1 credit = ₹1 offset on power bill</div>
        </div>
        <div class="step-image">
            <img src="data:image/png;base64,{base64_image}" alt="Step 1 Image">
        </div>
    </div>
""".format(base64_image=base64_image), unsafe_allow_html=True)

# Step 2 (Reverse order: image on the left, text on the right)
st.markdown("""
    <div class="step-container" style="flex-direction: row-reverse;">
        <div class="step-text">
            <div class="step-number">Step 2</div>
            <div class="step-title">Track your savings</div>
            <div class="step-description">Monitor how much you're saving each month and watch your credits grow as your reserved solar panels generate power.</div>
            <div class="step-info">Real-time savings tracking</div>
        </div>
        <div class="step-image">
            <img src="data:image/png;base64,{base64_image}" alt="Step 2 Image">
        </div>
    </div>
""".format(base64_image=base64_image), unsafe_allow_html=True)

# Step 3
st.markdown("""
    <div class="step-container">
        <div class="step-text">
            <div class="step-number">Step 3</div>
            <div class="step-title">Enjoy reduced bills</div>
            <div class="step-description">Apply your earned credits to reduce your monthly power bill and enjoy the savings!</div>
            <div class="step-info">Automatic bill offset</div>
        </div>
        <div class="step-image">
            <img src="data:image/png;base64,{base64_image}" alt="Step 3 Image">
        </div>
    </div>
""".format(base64_image=base64_image), unsafe_allow_html=True)
import streamlit as st


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
        .info-box {
            background-color: #0b2a39;
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 20px;
        }
        .savings-range {
            font-size: 18px;
            margin-top: 15px;
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
        .reservation-fee-container {
            text-align: center;
            margin-top: 30px;
        }
    </style>
""", unsafe_allow_html=True)

# Main Container
st.markdown("""
    <div class="container">
        <div class="left-column">
            <div class="header">Forecast Your Savings</div>
            <div class="sub-header">Soho 195 <span style="background-color: #00D082; border-radius: 5px; padding: 3px 10px;">Operational Until 2039</span></div>
            <div>Every unit of electricity from this project generates ₹5.2 discount on your power bill</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# Input Fields and Sliders
avg_power_bill = st.number_input("Enter avg power bill", value=2500, min_value=0, step=100)
savings_range = st.slider("Choose savings range (%)", min_value=0, max_value=100, value=75)

# Calculations
monthly_savings = avg_power_bill * (savings_range / 100) * 0.075
reserved_solar = monthly_savings * 1.67
energy_produced = reserved_solar * 0.115
annual_savings = monthly_savings * 12
total_savings = annual_savings * 15
reservation_fee = reserved_solar * 48.81

# Display Metrics aligned horizontally
st.markdown("""
    <div class="metrics-container">
        <div class="metric-box">
            <h4>Your Monthly Savings</h4>
            <p>₹{monthly_savings:,.2f}</p>
            <small>Amount saved monthly</small>
        </div>
        <div class="metric-box">
            <h4>Reserved Solar</h4>
            <p>{reserved_solar:,.2f} W</p>
            <small>Total solar reserved</small>
        </div>
        <div class="metric-box">
            <h4>Energy Produced / Mo</h4>
            <p>{energy_produced:,.2f} kWh</p>
            <small>Energy produced monthly</small>
        </div>
        <div class="metric-box">
            <h4>Annual Savings</h4>
            <p>₹{annual_savings:,.2f}</p>
            <small>Total annual savings</small>
        </div>
        <div class="metric-box">
            <h4>15 Year Savings</h4>
            <p>₹{total_savings:,.2f}</p>
            <small>Total savings over 15 years</small>
        </div>
    </div>
""".format(
    monthly_savings=monthly_savings,
    reserved_solar=reserved_solar,
    energy_produced=energy_produced,
    annual_savings=annual_savings,
    total_savings=total_savings
), unsafe_allow_html=True)

# Display One-time Reservation Fee centered
st.markdown("""
    <div class="reservation-fee-container">
        <h4>One-time Reservation Fee</h4>
        <p>₹{reservation_fee:,.2f}</p>
        <small>Click the button below to get started for free!</small>
        <button class="button">Get Started for Free</button>
    </div>
""".format(reservation_fee=reservation_fee), unsafe_allow_html=True)
