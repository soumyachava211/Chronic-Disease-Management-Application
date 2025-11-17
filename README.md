# Diabetes Self-Management Tracking System

This project implements a Python-based chronic disease self-management app for diabetes.  
It supports glucose tracking, medication adherence monitoring, trend analysis, and visual insights.

---

## 🔍 Features

✔ Import glucose readings  
✔ Classify readings (low, normal, high)  
✔ Compute daily statistics  
✔ Track medication adherence  
✔ Identify weekly patterns  
✔ Detect high-glucose trends  
✔ Generate visualizations (in notebook)  
✔ Configurable target ranges  

---

## 📂 Project Structure

diabetes-self-management-app/
│
├── data/ # glucose and medication logs
├── src/ # core app logic
├── notebooks/ # analysis & visualization
├── config/ # thresholds (optional)
├── requirements.txt
└── README.md

---

## ▶️ How to Run

Install requirements:

Load and analyze:
```python
from src.glucose_processing import *
df = load_glucose_data("data/glucose_readings.csv")
df = add_glucose_categories(df)

📊 Skills Demonstrated

Python data processing

Data validation

Trend analysis

Basic analytics and visualization

Chronic disease monitoring workflows

Clinical informatics concepts

🔒 Notes

This project is coursework only — no patient data is used.
