import streamlit as st
import requests
import json

st.set_page_config(page_title="Sentiment Analysis (Bahasa Melayu)")

# Title of the webpage
st.title("Sentiment Analysis (Bahasa Melayu)")

# Create an empty container to hold the user input
user_input_container = st.empty()

# Get user inputs
#sentence = user_input_container.text_area(label='Input a sentence in Malay to determine its sentiment.')
sentence = user_input_container.text_area(label='Isi ayat dalam Bahasa Melayu untuk menentukan sentimennya. 🇸🇬🇲🇾🇧🇳🇮🇩')

# Display the inputs
user_input = {"sentences": [sentence]} 
st.write("User input:")
st.write(user_input)

# Code to post the user inputs to the API and get the predictions
# Paste the URL to your GCP Cloud Run API here!
api_url = 'https://malay-sentiment-nqaybcgjca-as.a.run.app'  # replace with own Google Cloud Run API
api_route = '/predict_sentiment'

# Add a submit button
if st.button("Submit"):  # only display model predictions on UI if user clicks "Submit" button
    response = requests.post(f'{api_url}{api_route}', json=user_input)
    predictions = response.json()  # return dictionary with key 'predictions' & values are a list of predictions
    
    st.write(f"Prediction: {predictions}")  # prediction values were stored in 'predictions' key of dict: predictions. [0] is to give prediction output 0/1 in a "unlisted" format since we're only sending user inputs for 1 row of X at a time
   # Extract the sentiment probability from the dictionary
    probability = predictions["probability"][0]

    # Create a dictionary to pass to st.bar_chart and round the values
    chart_data = {
        "Sentiment": ["Negative", "Not Negative"],
        "Probability": [probability, 1 - probability]
    }

    # Create a bar chart
    st.bar_chart(chart_data, x="Sentiment", y="Probability", use_container_width=True, orientation = 'h')