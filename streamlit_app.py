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


# Code to post the user inputs to the API and get the predictions
# Paste the URL to your GCP Cloud Run API here!
api_url = 'https://malay-sentiment-nqaybcgjca-as.a.run.app' # replace with own Google Cloud Run API
api_route = '/predict_sentiment'

# Add a submit button
if st.button("Submit"): # only display model predictions on UI if user clicks "Submit" button
    response = requests.post(f'{api_url}{api_route}', json=json.dumps(user_input)) # json.dumps() converts dict to JSON
    predictions = response.json() # return dictionary with key 'predictions' & values are a list of predictions
    
    st.write(f"Prediction: {predictions['predictions'][0]}") # prediction values were stored in 'predictions' key of dict: predictions. [0] is to give prediction output 0/1 in a "unlisted" format since we're only sending user inputs for 1 row of X at a time
# See the 3: docker notebook to see why. basically it's to pull the value from the dictionary: {'predictions': [0, 1, 1, 1, 0]}