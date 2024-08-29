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
