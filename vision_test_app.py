# Import necessary libraries and modules
from dotenv import load_dotenv
import os
import streamlit as st
from PIL import Image
import google.generativeai as ga_api
load_dotenv()

# Configure the API key for Google's generative AI services
ga_api.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Define a function to fetch response from Gemini model based on input and image
def fetch_ai_response(prompt_text, image_file):
    ai_model = ga_api.GenerativeModel('gemini-pro-vision')
    response = ai_model.generate_content([prompt_text, image_file] if prompt_text else image_file)
    return response.text

# Streamlit app configuration for page setup
st.set_page_config(page_title="Gemini Vision Demo")

# App header
st.header("Gemini Vision Exploration")

# User input for text prompt
user_prompt = st.text_input("Enter your prompt:", key="prompt")

# Image upload section
user_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# Initialize image variable
processed_image = ""

# Process the uploaded image and display
if user_image is not None:
    processed_image = Image.open(user_image)
    st.image(processed_image, caption="Your Uploaded Image", use_column_width=True)

# Submit button for processing
if st.button("Generate Response"):
    ai_response = fetch_ai_response(user_prompt, processed_image)
    st.subheader("AI Generated Response")
    st.write(ai_response)
