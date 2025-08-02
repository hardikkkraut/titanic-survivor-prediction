import streamlit as st
import pandas as pd
import numpy as np
import joblib

model = joblib.load("random_forest_model.pkl")

st.title("🚢 Titanic Survivor Predictor")

pclass = st.selectbox("Passenger Class (1 = 1st, 2 = 2nd, 3 = 3rd)", [1, 2, 3])
age = st.slider("Age", 1, 80, 25)
sibsp = st.slider("Number of siblings/spouses aboard", 0, 8, 0)
parch = st.slider("Number of parents/children aboard", 0, 6, 0)
fare = st.slider("Fare Paid", 0, 500, 50)
sex_male = st.selectbox("Sex", ["female", "male"]) == "male"
embarked_Q = st.selectbox("Embarked at Q?", ["No", "Yes"]) == "Yes"
embarked_S = st.selectbox("Embarked at S?", ["No", "Yes"]) == "Yes"

features = np.array([[pclass, age, sibsp, parch, fare, sex_male, embarked_Q, embarked_S]])
prediction = model.predict(features)[0]

if st.button("Predict"):
    st.success("🧍 Survived" if prediction else "💀 Did Not Survive")

import joblib
joblib.dump(rf, "random_forest_model.pkl")
