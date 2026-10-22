# 📅 Week 9 — Model Deployment

## 📖 Overview

BinX Tech — AI & Machine Learning Internship Program

This folder contains my Week 9 work: deploying machine learning models and building interactive applications. The week focuses on model serialization, FastAPI, Streamlit, public hosting, and project preparation for the final presentation.

The work is applied to the Cardiovascular Disease project, starting with saving the trained neural network and preprocessing objects, then building a prediction API and an interactive dashboard before deploying the application publicly.

## 📚 Days

- ✅ **Day 1 — Sprint 4 Planning, Model Serialization & MLOps**
- ✅ **Day 2 — Serving the Model with FastAPI**
- ✅ **Day 3 — Building an Interactive Streamlit Dashboard**
- ✅ **Day 4 — Public Deployment & Environment Configuration**
- ✅ **Day 5 — Repository Polish, Definition of Done & Sprint Review**

## 🛠️ Technologies

Python, TensorFlow, Keras, FastAPI, Pydantic, Uvicorn, Streamlit, Joblib, Scikit-learn, Pandas, NumPy, Git, GitHub, Hugging Face Spaces, Render

## 📂 Repository Structure

```text
week9/
│
├── day1/
│   ├── day1.ipynb
│   ├── README.md
│   ├── cardio_cleaned.csv
│   ├── final_neural_network.keras
│   ├── mlflow.db
│   ├── requirements.txt
│   ├── standard_scaler.joblib
│   └── best_threshold.txt
│
├── day2/
│   ├── day2.ipynb
│   ├── README.md
│   ├── standard_scaler.joblib
│   └── final_neural_network.keras
│
├── day3/
│   ├── app.py
│   ├── day3.ipynb
│   ├── .gitignore
│   ├── README.md
│   ├── standard_scaler.joblib
│   └── final_neural_network.keras
│
├── day4/
│   ├── README.md
│   ├── .python-version
│   ├── app.py
│   ├── standard_scaler.joblib
│   ├── requirements.txt
│   └── final_neural_network.keras
│
├── day5/
│   ├── README.md
│   └── day5.ipynb
│
└── README.md
```

## 🎯 Key Learning Outcomes

- Saving trained models and preprocessing objects for reuse.
- Building REST APIs with FastAPI and validating inputs with Pydantic.
- Developing interactive machine learning applications using Streamlit.
- Deploying applications using public hosting platforms.
- Maintaining consistent preprocessing between training and deployment.
- Improving project organization, documentation, and reproducibility.

## 🚀 Practical Project

**Project:** Cardiovascular Disease Prediction System

The practical work focuses on deploying a trained neural network to predict cardiovascular disease based on user-provided health features.

The project integrates the saved model and scaler with a FastAPI prediction endpoint and a Streamlit dashboard, making the model accessible through an interactive application.

## 📌 Summary

Week 9 focused on transforming a trained machine learning model into a functional, publicly accessible application. It covered API development, interactive dashboards, deployment, reproducibility, and final project preparation.
