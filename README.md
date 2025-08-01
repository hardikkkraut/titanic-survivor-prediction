# 🚢 Titanic Survival Prediction – Machine Learning Project

Predicting which passengers survived the Titanic tragedy using various machine learning models.

---

## 📂 Project Overview

This project uses the Kaggle Titanic dataset to build and evaluate predictive models.  
It covers the full ML workflow: data cleaning, feature engineering, model training, evaluation, and basic web deployment.

---

## 📊 Dataset

- Source: [Kaggle Titanic: Machine Learning from Disaster](https://www.kaggle.com/competitions/titanic/data)
- File used: `train.csv`

---

## 🧠 Models Used

- **Logistic Regression**
- **Decision Tree**
- **Random Forest**

Each model was evaluated using accuracy, precision, recall, and F1-score.

---

## 🔍 Evaluation Metrics

| Model               | Accuracy | Precision | Recall | F1 Score |
|---------------------|----------|-----------|--------|----------|
| Logistic Regression | 81%      | 77%       | 75%    | 76%      |
| Decision Tree       | 78%      | 72%       | 74%    | 73%      |
| Random Forest       | 84%      | 82%       | 81%    | 81%      |

✅ **Random Forest performed best** overall.

---

## 📉 Visualizations

| Chart                         | Description                            |
|------------------------------|----------------------------------------|
| `survival_count.png`         | Bar plot of total survivors vs. deaths |
| `age_distribution.png`       | Histogram of passenger ages            |
| `rf_confusion_matrix.png`    | Confusion matrix for Random Forest     |
| `rf_roc_curve.png`           | ROC curve for Random Forest            |

You can find these visualizations in the project folder.

---

## 🌐 Streamlit App

Interactive prediction app built using **Streamlit**.

### ▶️ How to Run:

```bash
pip install -r requirements.txt
streamlit run app.py
