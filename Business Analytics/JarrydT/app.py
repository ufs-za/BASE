pip install streamlit
import pickle
import streamlit as st
import pickle
import numpy as np
from google.colab import drive 

# Load the Random Forest model from the Pickle file
with open('RandomForestModel.pkl', 'rb') as file:
    model = pickle.load(file)

# Define function for predicting Purchase Intention
def predict_purchase_intention(inputs):
    prediction = model.predict([inputs])
    return prediction

# Set up Streamlit app title
st.title("Purchase Intention Prediction App")

# Create the input fields for the 9 features
st.header("Please input the following information:")

# Creating inputs for 9 variables
Type_of_Customer = st.radio('Are you a regular (1) or need-based customer (2):', [1, 2])
EAverage = st.radio('How empathetic are the employees of the store?', [1, 2, 3, 4, 5])
CAverage = st.radio('How convenient is it for you to shop at the store?', [1, 2, 3, 4, 5])
PSAverage = st.radio('How price sensitive are you?', [1, 2, 3, 4, 5])
PEAverage = st.radio('How comfortable are you in the stores environment?', [1, 2, 3, 4, 5])
PPQAverage = st.radio('How satisfied are you with the product quality?', [1, 2, 3, 4, 5])
CTAverage = st.radio('How much do you trust the store?', [1, 2, 3, 4, 5])
PVAverage = st.radio('How satisfied are you with the value for money?', [1, 2, 3, 4, 5])

# When the user submits, we make a prediction
if st.button('Predict Purchase Intention'):
    # Collect the inputs into a list
    user_input = np.array([Type_of_Customer, EAverage, CAverage, PSAverage, PEAverage, PPQAverage, CTAverage, PVAverage])

    # Make prediction
    prediction = predict_purchase_intention(user_input)

    # Display the predicted Purchase Intention level
    st.subheader(f"Predicted Purchase Intention Level: {prediction[0]}")

    accuracy = 0.7529  
    st.write(f"Model Accuracy: {accuracy * 100:.2f}%")
