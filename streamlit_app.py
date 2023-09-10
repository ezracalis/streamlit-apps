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
    # Extract the sentiment probability from the dictionary
    probability = predictions["probability"][0]

    # Create a DataFrame for the chart
    chart_data = pd.DataFrame({
        "Sentiment": ["Negative", "Not Negative"],
        "Probability": [probability, 1 - probability],
        "Color": ["Negative", "Not Negative"]
    })

    # Create a custom bar chart using Altair
    chart = alt.Chart(chart_data).mark_bar().encode(
        x="Sentiment",
        y="Probability",
        color=alt.Color("Color", scale=alt.Scale(domain=["Negative", "Not Negative"], range=["#FC8282", "#82E0FC"])),
        tooltip=["Sentiment", "Probability"]
    ).properties(
        width=alt.Step(80)
    )

    # Display the chart
    st.altair_chart(chart, use_container_width=True)