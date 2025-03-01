import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API Key
load_dotenv()
API_KEY = "AIzaSyAWLull5zONsH_IZwQ8mvQq_mOdAO69UyU"
GEMINI_API_KEY = os.getenv(API_KEY)

# Configure Google Gemini API
genai.configure(api_key=GEMINI_API_KEY)

# AI Function
def get_medicine_recommendation(symptoms):
    try:
        model = genai.GenerativeModel("gemini-pro")
        prompt = f"I have the following symptoms: {symptoms}. Suggest possible medicines and precautions."
        response = model.generate_content(prompt)
        
        # Formatting the response in the desired output format
        output = f"Based on the symptoms you provided ({symptoms}), here are some possible treatments:\n\n"

        # Split response into medicines and precautions
        medicines, precautions = response.text.split('**Precautions:**')

        output += f"{medicines.strip()}\n\n"
        output += f"**Precautions:** {precautions.strip()}\n"
        output += "Always consult a healthcare professional before starting any new medication."
        
        return output
    
    except Exception as e:
        return f"Error: {e}"

# Streamlit UI with Custom CSS
st.set_page_config(page_title="AI Medical Assistant", page_icon="🩺")

st.markdown("""
    <style>
        body {
            background-color: #f8f9fa;
        }
        .main-title {
            text-align: center;
            font-size: 32px;
            color: #007bff;
        }
        .stTextArea {
            border-radius: 10px;
            border: 1px solid #007bff;
        }
        .stButton>button {
            background-color: #007bff;
            color: white;
            border-radius: 10px;
            padding: 10px;
        }
        .stButton>button:hover {
            background-color: #0056b3;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.header("App Functionalities")
st.sidebar.write("""
- **Symptom Input**: Enter symptoms to get possible medicine recommendations.
- **Medicine & Precautions**: Get suggestions for medicines and precautions based on your input.
- **Developed By**: Darshanikanta
""")

# UI Elements
st.markdown("<h1 class='main-title'>🩺 AI-Powered Medical Assistant</h1>", unsafe_allow_html=True)
st.write("Enter your symptoms below, and AI will suggest possible medicines.")

symptoms = st.text_area("Describe your symptoms:", placeholder="E.g., headache, fever, body pain...")

if st.button("Get Medicine Recommendation"):
    if symptoms:
        ai_response = get_medicine_recommendation(symptoms)
        st.subheader("🔹 AI Suggested Medicines & Precautions")
        st.write(ai_response)
    else:
        st.warning("Please enter your symptoms to proceed.")

st.write("**Disclaimer:** This is not a substitute for professional medical advice. Please consult a healthcare provider.")
