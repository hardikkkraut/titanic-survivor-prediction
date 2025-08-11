import streamlit as st
import joblib
import numpy as np
from PIL import Image
import time
from streamlit.components.v1 import html

# -----------------------
# Load model
# -----------------------
model = joblib.load('model.pkl')

# -----------------------
# Page Config
# -----------------------
st.set_page_config(
    page_title="Titanic Survival Predictor",
    page_icon="🚢",
    layout="centered"
)

# -----------------------
# Header
# -----------------------
st.markdown(
    """
    <h1 style='text-align: center; color: #2E86C1;'>🚢 Titanic Survival Prediction App</h1>
    <p style='text-align: center;'>Will you survive the most famous shipwreck in history? 🕵️‍♂️</p>
    """,
    unsafe_allow_html=True
)

# Optional Titanic image
image = Image.open("image.png")  # Make sure image.png is in your project folder
st.image(image, use_container_width=True)

st.markdown("---")

# -----------------------
# Inputs (2-column layout)
# -----------------------
col1, col2 = st.columns(2)

with col1:
    pclass = st.selectbox("🎟 Passenger Class", [1, 2, 3])
    sex = st.selectbox("⚧ Sex", ["male", "female"])
    age = st.slider("🎂 Age", 0, 100, 25)

with col2:
    sibsp = st.number_input("👨‍👩‍👧‍👦 Siblings/Spouses Aboard", 0, 10, 0)
    parch = st.number_input("👶 Parents/Children Aboard", 0, 10, 0)
    fare = st.number_input("💰 Fare Paid", 0.0, 600.0, 32.0)
    embarked = st.selectbox("🛳 Port of Embarkation", ["C", "Q", "S"])

# -----------------------
# Encoding
# -----------------------
sex_encoded = 1 if sex == "male" else 0
embarked_map = {"C": 0, "Q": 1, "S": 2}
embarked_encoded = embarked_map[embarked]

features = np.array([[pclass, sex_encoded, age, sibsp, parch, fare, embarked_encoded]])

# -----------------------
# Prediction Button with Progress Bar and Confetti
# -----------------------
if st.button("🔍 Predict Survival"):
    progress_bar = st.progress(0)
    status_text = st.empty()

    for percent_complete in range(0, 101, 10):
        progress_bar.progress(percent_complete)
        status_text.text(f"Analyzing passenger details... {percent_complete}%")
        time.sleep(0.2)

    prediction = model.predict(features)
    progress_bar.empty()
    status_text.empty()

    if prediction[0] == 1:
        st.success("🎉 This passenger **would have SURVIVED**! 🏆")
        st.balloons()

        confetti_js = """
        <canvas id="confetti"></canvas>
        <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.4.0/dist/confetti.browser.min.js"></script>
        <script>
        var duration = 3 * 1000;
        var end = Date.now() + duration;

        (function frame() {
            confetti({
                particleCount: 5,
                angle: 60,
                spread: 55,
                origin: { x: 0 }
            });
            confetti({
                particleCount: 5,
                angle: 120,
                spread: 55,
                origin: { x: 1 }
            });

            if (Date.now() < end) {
                requestAnimationFrame(frame);
            }
        }());
        </script>
        """
        html(confetti_js, height=200)
    else:
        st.error("☠️ Unfortunately, this passenger **would NOT have survived**.")

    st.markdown("---")
    st.markdown("**📊 Did you know?** In reality, only about **38%** of passengers survived the Titanic disaster.")
