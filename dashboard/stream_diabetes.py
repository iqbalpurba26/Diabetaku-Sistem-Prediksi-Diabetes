import joblib
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

diabetes_model = joblib.load("../model/diabetes_model.sav")
df = pd.read_csv('diabets_dataset_clean.csv')

X = df.drop(columns='diabetes', axis=1)
scaler = StandardScaler()


st.set_page_config(
    page_title="DiabetaKu",
    layout="wide",
    page_icon="asset/diabetes_icon.png"
)
# Title Website
st.title('DiabetaKu : Aplikasi Prediksi Diabetes')

col1, col2 = st.columns(2)

with col1:
    Gender = st.text_input('Gender (0 : Female, 1 : Male) : ')

with col1:
    Age = st.text_input("Your Age :")

with col1:
    Hipertension = st.text_input('Have hipertension? (1 : yes, 0 : no) : ')

with col1:
    Heart_disease = st.text_input('Have heart disease? (1 : yes, 0 : no) : ')

with col2:
    Smoking_history = st.text_input(
        "Are You Smooking? (-1 : No Info, 0 : never, 1 : former, 2 : current, 3 : not current, 4 : ever) : ")
with col2:
    bmi = st.text_input('Your BMI : ')

with col2:
    HbA1c_level = st.text_input("Level Hemoglobin A1c : ")

with col2:
    Blood_glucose = st.text_input('Level Blood Glucose : ')

input_data = pd.to_numeric([Gender, Age, Hipertension, Heart_disease,
                           Smoking_history, bmi, HbA1c_level, Blood_glucose], errors='coerce')
input_data_array = np.array(input_data)
input_reshape = input_data_array.reshape(1, -1)
scaler.fit(X)
std_data = scaler.transform(input_reshape)

diabetes_diagnosis = "BELUM MELENGKAPI DATA"

if st.button('Prediction'):
    diabetes_prediction = diabetes_model.predict(std_data)
    if (diabetes_prediction[0] == 0):
        diabetes_diagnosis = "PASIEN TIDAK TERKENA DIABETS"
    else:
        diabetes_diagnosis = "PASIEN TERKENA DIABETES"

st.subheader("Hasil Prediksi Adalah")
st.success(diabetes_diagnosis)
