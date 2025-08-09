🚢 Titanic Survival Prediction – Machine Learning + Streamlit
Predict survival on the Titanic using Machine Learning, visualize results, and interact with the model in a Streamlit app.

This project uses the famous Titanic dataset to train a Random Forest Classifier that predicts whether a passenger would survive or not. Alongside predictions, it includes rich visualizations and a fun CSV output with emojis 🎉.
___

📂 Project Structure
bash
Copy
Edit
titanic-survivor-prediction/
│
├── train.csv                  # Training data
├── test.csv                   # Test data
├── titanic_survival.ipynb     # Jupyter Notebook (training + visualization)
├── app.py                     # Streamlit app for interactive predictions
├── model.pkl                  # Saved Random Forest model
├── submission.csv             # Kaggle-ready predictions
├── submission_fun.csv         # Creative predictions with emojis
└── README.md                  # Project documentation

___

✨ Features
Model Training

Random Forest Classifier trained on Titanic dataset

Preprocessing: handling missing values, encoding categorical data

Batch Predictions

submission.csv → standard Kaggle format

submission_fun.csv → includes emojis, custom messages, and confidence scores

Visualizations (Saved as PNG)

Confusion Matrix

ROC Curve

Survival Count Plot

Age Distribution Plot

Interactive Web App (Streamlit)

Input passenger details

Get real-time survival prediction + probability score

___

🚀 How to Run
1️⃣ Train the Model & Generate Files
bash
Copy
Edit
jupyter notebook titanic_survival.ipynb
This will train the model, generate visualizations, and create both CSV files.

2️⃣ Run the Streamlit App
bash
Copy
Edit
streamlit run app.py
Open the link in your browser to interact with the model.

___

📊 Example Fun CSV Output
PassengerId	Survived	Survival_Status	Message	Confidence_Score
892	0	Not Survived ❌	Better luck next time 🚢💦	0.13
893	1	Survived ✅	You’re a survivor! 🎉	0.91

___

🛠 Tech Stack
Python

Pandas, NumPy – Data preprocessing

Scikit-learn – Machine learning model

Matplotlib, Seaborn – Data visualization

Streamlit – Web app interface