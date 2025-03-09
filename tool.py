import streamlit as st  # type: ignore
import re

# Page Configuration
st.set_page_config(page_title="Password Strength Meter", page_icon="🔒")

# Custom CSS for Background and Input Box
st.markdown("""
    <style>
        div[data-testid="stAppViewContainer"] {
            background-color: #E6E6FA; /* Light Purple Background */
        }
        input[type="password"] {
            background-color: #FFC0CB !important; /* Pink Input Box */
            color: blue !important; /* Text Color */
            border-radius: 10px; /* Rounded Corners */
            padding: 10px; /* Padding */
        }
    </style>
""", unsafe_allow_html=True)

# Title and Description
st.title("🔐 Password Strength Meter")
st.markdown("""
    ## Welcome to the Password Strength Meter App! 👏  
    Use this simple tool to check the strength of your password.  
    We will give you tips to protect your account with a **Strong Password** 🔒.
""")

# Password Input
password = st.text_input("Enter your password", type="password")

# Initialize feedback and score
feedback = []
score = 0

if password:  # If password is entered
    # Condition 1: Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("🔴 Password should be at least 8 characters long.")

    # Condition 2: Uppercase and lowercase check (Fixed mistake)
    if re.search("[a-z]", password) and re.search("[A-Z]", password):  # Fixed [a-z] typo
        score += 1
    else:
        feedback.append("😒 Password should contain both uppercase and lowercase letters.")

    # Condition 3: Digit check
    if re.search("[0-9]", password):
        score += 1
    else:
        feedback.append("🫥 Password should contain at least one digit.")

    # Condition 4: Special character check
    if re.search("[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("😶‍🌫️ Password should contain at least one special character (!@#$%^&*).")

    # Final feedback based on score
    if score == 4:
        feedback.append("🟢 Your Password is **Strong**! 🎉")
    elif score == 3:
        feedback.append("🟡 Good Password, but it could be stronger!")
    else:
        feedback.append("🔴 Weak Password. Please make it stronger!")

    # Display feedback
    st.markdown("## 🔎 Suggestions For Improvement:")
    for tip in feedback:
        st.write(tip)

else:
    st.info("🔹 Please enter your password to get started!")
