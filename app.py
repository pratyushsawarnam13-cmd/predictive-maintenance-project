import streamlit as st
import pandas as pd
import joblib

st.title("Engine Predictive Maintenance")

# Load model
model = joblib.load("best_model.joblib")

st.write("Enter engine details:")

rpm = st.number_input("Engine RPM")
lub_oil_pressure = st.number_input("Lub Oil Pressure")
fuel_pressure = st.number_input("Fuel Pressure")
coolant_pressure = st.number_input("Coolant Pressure")
lub_oil_temp = st.number_input("Lub Oil Temp")
coolant_temp = st.number_input("Coolant Temp")

if st.button("Predict"):
    input_data = pd.DataFrame([[rpm, lub_oil_pressure, fuel_pressure,
                                coolant_pressure, lub_oil_temp, coolant_temp]],
                              columns=['Engine_rpm','Lub_oil_pressure','Fuel_pressure',
                                       'Coolant_pressure','lub_oil_temp','Coolant_temp'])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("Engine needs maintenance")
    else:
        st.success("Engine is normal")
