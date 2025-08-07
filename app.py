import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load('model.pkl')

st.title("🚢 Titanic Survival Prediction App")

# User inputs
pclass = st.selectbox("Passenger Class (1 = 1st, 2 = 2nd, 3 = 3rd)", [1, 2, 3])
sex = st.selectbox("Sex", ["male", "female"])
age = st.slider("Age", 0, 100, 25)
sibsp = st.number_input("Number of Siblings/Spouses Aboard", 0, 10, 0)
parch = st.number_input("Number of Parents/Children Aboard", 0, 10, 0)
fare = st.number_input("Fare Paid", 0.0, 600.0, 32.0)
embarked = st.selectbox("Port of Embarkation", ["C", "Q", "S"])

# Encode inputs
sex_encoded = 1 if sex == "male" else 0
embarked_map = {"C": 0, "Q": 1, "S": 2}
embarked_encoded = embarked_map[embarked]

# Prepare feature vector
features = np.array([[pclass, sex_encoded, age, sibsp, parch, fare, embarked_encoded]])

# Prediction
if st.button("Predict"):
    prediction = model.predict(features)
    if prediction[0] == 1:
        st.success("🎉 This passenger would have SURVIVED.")
    else:
        st.error("☠️ Unfortunately, this passenger would NOT have survived.")
