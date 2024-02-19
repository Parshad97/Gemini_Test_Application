# Import required modules and libraries
from dotenv import load_dotenv
import os
import streamlit as web_interface
import google.generativeai as ai_generator

load_dotenv()

# Set up the API for Google's generative AI service
ai_generator.configure(api_key=os.getenv("GEN_AI_API_KEY"))

# Instantiate the generative AI model
ai_model = ai_generator.GenerativeModel("gemini-pro")

# Function to query the AI model and get responses
def query_ai_model(query_text):
    ai_response = ai_model.generate_content(query_text)
    return ai_response.text

# Web app configuration and layout
web_interface.set_page_config(page_title="Interactive Q&A with Gemini")
web_interface.header("Gemini Q&A Interface")

# User input field
user_query = web_interface.text_input("Please enter your question:", key="user_query")

# Button to submit the query
query_submit = web_interface.button("Submit Question")

# Displaying the response from the AI model
if query_submit:
    response_text = query_ai_model(user_query)
    web_interface.subheader("Gemini's Answer")
    web_interface.write(response_text)
