import pandas as pd
import numpy as np
import streamlit as st
import pickle

# Load the trained model
with open('Fraud_Detection.pkl', 'rb') as file:
    model = pickle.load(file)


# Define a function to make predictions
def predict_fraud(features):
    return model.predict([features])[0]

# Streamlit app
st.title('Fraud Detection')

st.write("Enter the details below:")

# Input fields for model features
feature1 = st.number_input('Amount of the transaction in local currency', value=0.0)
feature2 = st.number_input('newbalanceOrig-oldbalanceOrig', value=0.0)
feature3 = st.number_input('newbalanceDest-oldbalanceDest', value=0.0)
feature4 = st.number_input('type_TRANSFER', value=0.0)
feature5 = st.number_input('type_CASH_OUT', value=0.0)
# Add more inputs as needed

# Button to make prediction
if st.button('Predict'):
    features = [feature1, feature2, feature3, feature4,feature5]  # Add all feature inputs
    prediction = predict_fraud(features)
    st.write(f'Prediction:   {"Fraud" if prediction == 1 else "Legitimate"}')