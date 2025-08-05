import streamlit as st
import pandas as pd
import joblib

# Load model
rf = joblib.load("random_forest_model.pkl")

# Title and info
st.set_page_config(page_title="Titanic Survivor Predictor", layout="centered")
st.title("🚢 Titanic Survivor Predictor")
st.markdown("""
This app predicts whether a passenger would have survived the Titanic disaster based on their details.
""")

# Sidebar input
st.sidebar.header("Passenger Details")
pclass = st.sidebar.selectbox("Passenger Class", [1, 2, 3])
sex = st.sidebar.radio("Sex", ["male", "female"])
age = st.sidebar.slider("Age", 0, 80, 25)
sibsp = st.sidebar.slider("# of Siblings/Spouses", 0, 5, 0)
parch = st.sidebar.slider("# of Parents/Children", 0, 5, 0)
fare = st.sidebar.slider("Fare Paid", 0.0, 500.0, 50.0)
embarked = st.sidebar.selectbox("Port of Embarkation", ["S", "C", "Q"])

# Raw input DataFrame
raw_input = pd.DataFrame({
    'Pclass': [pclass],
    'Age': [age],
    'Fare': [fare],
    'SibSp': [sibsp],
    'Parch': [parch],
    'Sex': [sex],
    'Embarked': [embarked]
})

# Apply the same encoding used during training
input_data = pd.get_dummies(raw_input)

# Match the training features exactly
input_data = input_data.reindex(columns=rf.feature_names_in_, fill_value=0)

# Predict button
if st.button("Predict Survival"):
    prediction = rf.predict(input_data)[0]
    proba = rf.predict_proba(input_data)[0][1]

    if prediction == 1:
        st.success(f"🎉 The passenger would have SURVIVED! (Confidence: {proba:.2%})")
    else:
        st.error(f"❌ The passenger would NOT have survived. (Confidence: {1 - proba:.2%})")

st.markdown("---")
st.subheader("Model Input Features")

