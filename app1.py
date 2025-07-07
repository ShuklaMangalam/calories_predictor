import streamlit as st
import numpy as np
import joblib
from xgboost import XGBRegressor
model = joblib.load("model1.pkl")

st.title("Calories Burnt Prediction")
st.divider()
st.write("this ml app helps you predict the the no of calories burnt during excercies while using parameter such as height, weight, age ,durations and gender")

st.divider()
Height= st.number_input("Your height in cms", min_value = 0,value= 140)
Weight =st.number_input("Your weight in kgs", min_value = 0,value =50)
Age=st.number_input("Your age ", min_value = 0, value =45)
Duration = st.number_input("Duration in mins", min_value = 0,value = 20)
Gender = st.selectbox("Choose your Gender", ["Male","Female"])
gender_num = 1 if Gender == "Male" else 0

st.divider()

x =[[Height, Weight,Age,Duration,gender_num]]
predictbutton = st.button("Predict")

if predictbutton:
    st.balloons()
    x_array =np.array(x)
    prediction = model.predict(x_array)
    st.write(f"The predicted calories is {prediction}")
else : st.write("click the predict button")

