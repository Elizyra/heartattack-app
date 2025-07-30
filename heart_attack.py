
import streamlit as st
import joblib

# Load model
model = joblib.load('Heart_Attack_P')

# Page config
st.set_page_config(page_title="Heart Attack Analysis", layout="wide")

# Title
st.title("Heart Attack Prediction Dashboard")

# Arrangement for the columns
col1, col2 = st.columns(2)  # Fixed typo: 'column' -> 'columns'

# Input fields
age = col1.number_input('Enter Your Age', min_value=14, max_value=103, step=1)
gender = col2.selectbox('Select Your Gender', options=['Male', 'Female'])
heart_rate = col1.number_input('Enter Your Heart rate', min_value=20, max_value=1111, step=1)
systolic_bp = col2.number_input('Enter Your Systolic blood pressure', min_value=42, max_value=223, step=1)
diastolic_bp = col1.number_input('Enter Your Diastolic blood pressure', min_value=38, max_value=154, step=1)
blood_sugar = col2.number_input('Enter Your Blood Sugar level', min_value=35.0, max_value=541.0, step=0.01)
ck_mb = col1.number_input('Enter Your CK-MB', min_value=0.000, max_value=300.0, step=0.001)
troponin = col2.number_input('Enter Your Troponin', min_value=0.000, max_value=10.3, step=0.001)


# Convert gender to numerical (Male=1, Female=0)
gender_num = 1 if gender == 'Male' else 0


# Creating Prediction
if st.button('Check if the patient has a heart attack'):
    # Prepare input data as a 2D array in the correct order
    input_data = [[
        age, 
        gender_num,
        heart_rate,
        systolic_bp,
        diastolic_bp,
        blood_sugar,
        ck_mb,
        troponin
    ]]
    
    prediction = model.predict(input_data)
    
    if prediction[0] == 1:
        st.error('The patient has a heart attack risk')  # Fixed: st.positive -> st.error
    else:
        st.success('The patient does not have heart attack risk')  # Fixed: st.negative -> st.success


