#Import relevant packages
import pandas as pd
import streamlit as st
import numpy as np
from PIL import Image

# Load the Random Forest model from the Pickle file
model = pd.read_pickle("Model.pkl")

# Define the function for predicting Purchase Intention
def predict_purchase_intention(inputs):
    prediction = model.predict([inputs])
    prediction_proba = model.predict_proba([inputs])
    confidence = np.max(prediction_proba)
    return prediction, confidence

#Import the image and create a variable for it.
img = Image.open("PurchaseIntentionImage.jpg")

#Create styling to hide menu options and "made by streamlit" as well as making background white
hide_streamlit_style = """
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    textarea {
        background-color: white !important;
        color: black !important;
    }
    .big-font {
        font-size:20px !important;
    }
</style>
"""

#We set the page configuration to change the title and image of the page and set the layout to wide
st.set_page_config(page_title ='Purchase Intention Prediction', page_icon = img, layout="wide")

# Inject the custom CSS into the Streamlit app
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Set up the Streamlit app title
st.title("Purchase Intention Prediction App")

# Create a header
st.header("Please input the following information:")

#Create two different columns on the page, left and right.
left, right = st.columns(2, gap="large")  

#Create customer_type_map indicating that Regular Customer is equal to a 1 and Need-based Customer is a 2. 
#Needed to do this for the radio button
customer_type_map = {
    "Regular Customer": 1,
    "Need-based Customer": 2
}

#We first put down the radio buttton seperately, and plot it on the left side
with left:
    #Create a radio button and make the answers horizontally, then take the answer and run it through the customer_type_map for prediction
    selected_label = st.radio('What type of customer are you?', list(customer_type_map.keys()), horizontal=True)
    Type_of_Customer = customer_type_map[selected_label]

#On the right side we plot nothing
with right:
    st.write(" ")

# We use an expander to group the sliders
with st.expander("Customer Experience Ratings"):
    #Created two columns again for the sliders
    left, right = st.columns(2, gap="large")

    #These four sliders are plotted on the left side. The sliders are created with a range from 1-5.
    with left:
        EAverage = st.slider('How empathetic are the employees of the store?', 1, 5, help="1: Not empathetic, 5: Very empathetic")
        CAverage = st.slider('How convenient is it for you to shop at the store?', 1, 5, help="1: Not convenient, 5: Very convenient")
        PSAverage = st.slider('How price sensitive are you?', 1, 5, help="1: Not price sensitive, 5: Very price sensitive")
        PEAverage = st.slider('How comfortable are you in the store\'s environment?', 1, 5, help="1: Bad physical environment, 5: Great physical environment")
        
    #These three sliders are plotted on the left side. The sliders are created with a range from 1-5.
    with right:
        PPQAverage = st.slider('How satisfied are you with the product quality?', 1, 5, help="1: Bad product quality, 5: Amazing product quality")
        CTAverage = st.slider('How much do you trust the store?', 1, 5, help="1: Very low trust, 5: Very high trust")
        PVAverage = st.slider('How satisfied are you with the value for money?', 1, 5, help="1: Bad value for money, 5: Amazing value for money")

# Then it initialises the feedback state in session
if 'show_feedback' not in st.session_state:
    st.session_state['show_feedback'] = False
if 'show_feedback_box' not in st.session_state:
    st.session_state['show_feedback_box'] = False
    
#intention_map is created so that when the prediction of Purchase Intentions is made it is not just a value given.    
intention_map = {
    1: "Very Low (1)",
    2: "Low (2)",
    3: "Moderate (3)",
    4: "High (4)",
    5: "Very High (5)"
}

# A prediction is made when the user clicks the "Predict Purchase Intention" button
if st.button('Predict Purchase Intention'):
    # Collect the inputs into a list
    user_input = np.array([Type_of_Customer, EAverage, CAverage, PSAverage, PEAverage, PPQAverage, CTAverage, PVAverage])

    # The prediction is made
    prediction, confidence = predict_purchase_intention(user_input)

    # Display the predicted Purchase Intention level and the accuracy through the confidence level
    st.subheader(f"Predicted Purchase Intention Level: {intention_map[prediction[0]]}")
    st.write(f"Prediction Confidence: {confidence * 100:.2f}%")

    # Reveal "Give Feedback" link
    st.session_state['show_feedback'] = True

# Show feedback link if predictions are made
if st.session_state['show_feedback']:
    if st.button("Give Feedback"):
        st.session_state['show_feedback_box'] = True

# Show feedback box if give feedback is clicked for user to input feedback
if st.session_state['show_feedback_box']:
    feedback = st.text_area("Provide feedback on the prediction:")

    if st.button("Submit Feedback"):     
        # Immediately close the feedback dialog after submitting
        st.session_state['show_feedback_box'] = False
        st.session_state['show_feedback'] = False
        st.success("Your feedback has been received.")
        # Rerun the app after submission to reset the button
        st.rerun()
