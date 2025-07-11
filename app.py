import pandas as pd
import numpy as np
import pickle as pk
import streamlit as st
model = pk.load(open('House_prediction_model.pkl', 'rb'))
st.header("Pune House Price Predictor")

data=pd.read_csv('Cleaned Dataset.csv')

loc = st.selectbox("Select a Location", data['Location'].unique())
sqft = st.number_input("Enter Size (in sqft)", min_value=200, max_value=10000, value=1000)
beds = st.number_input("Flat Size (BHK)", min_value=1, max_value=10, value=2)
avail = st.selectbox("Availability", ['Ready to Move', 'Under Construction'])
furnishing = st.selectbox("Furnishing", ['furnished', 'semi-furnished', 'unfurnished'])
balcony = st.number_input("Number of Balconies", min_value=0, max_value=5, value=2)


input_data=pd.DataFrame(
    [[sqft, avail, furnishing, beds, loc, balcony,
      avail == 'Ready to Move', avail == 'Under Construction', furnishing == 'furnished'
         , furnishing == 'semi-furnished', furnishing == 'unfurnished']],
    columns=[
        'Size', 'Availability', 'Furnishing',
        'Flat Size', 'Location', 'Balcony',
        'Ready to Move', 'Under Construction',
        'furnished', 'semi-furnished', 'unfurnished'
    ])

if st.button("Predict Price"):
    prediction = model.predict(input_data)
    price = round(float(prediction[0]), 2)
    st.success(f"💰 Estimated Price: ₹ {price} Lakhs")