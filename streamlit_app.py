import streamlit as st
import requests
import json

# Title of the webpage
st.title("Sentiment Analysis (Bahasa Melayu 🇸🇬🇲🇾🇧🇳🇮🇩)")

# Create an empty container to hold the user input
user_input_container = st.empty()

# Get user inputs
sentence = user_input_container.text_area(label='Input a sentence in Malay to determine its sentiment.')

# Display the inputs
user_input = {"Sentence": sentence}
st.write("User input:")
st.write(user_input)

# Create buttons with words
button1 = st.button("Tahniah!")
button2 = st.button("Ape kau nyer problem eh")
button3 = st.button("Eh musibot, lu rilek sua")

# Define content for each button
content1 = "Tahniah!"
content2 = "Ape kau nyer problem eh"
content3 = "Eh musibot, lu rilek sua"

# Update the original text area based on the button clicked
if button1:
    user_input_container.text_area("Input a sentence in Malay to determine its sentiment.", content1)
    sentence = content1  # Update the 'sentence' variable
if button2:
    user_input_container.text_area("Input a sentence in Malay to determine its sentiment.", content2)
    sentence = content2  # Update the 'sentence' variable
if button3:
    user_input_container.text_area("Input a sentence in Malay to determine its sentiment.", content3)
    sentence = content3  # Update the 'sentence' variable
