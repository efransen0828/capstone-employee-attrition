import streamlit as st
import requests
import pandas as pd

# FastAPI endpoint URL (Ensure your FastAPI service is running)
API_URL = "http://127.0.0.1:8000/predict"

st.title("Employee Attrition Predictor")

st.write("Enter employee details to predict attrition risk.")

# Collect user input
employee_data = {
    "Age": st.number_input("Age", min_value=18, max_value=65, value=30),
    "DailyRate": st.number_input("Daily Rate", min_value=100, max_value=1500, value=800),
    "DistanceFromHome": st.number_input("Distance From Home", min_value=1, max_value=50, value=10),
    "EmployeeNumber": st.number_input("Employee Number", min_value=1, value=1),
    "EnvironmentSatisfaction": st.selectbox("Environment Satisfaction", [1, 2, 3, 4]),
    "HourlyRate": st.number_input("Hourly Rate", min_value=10, max_value=100, value=50),
    "JobInvolvement": st.selectbox("Job Involvement", [1, 2, 3, 4]),
    "JobLevel": st.selectbox("Job Level", [1, 2, 3, 4, 5]),
    "JobSatisfaction": st.selectbox("Job Satisfaction", [1, 2, 3, 4]),
    "MonthlyIncome": st.number_input("Monthly Income", min_value=1000, max_value=20000, value=5000),
    "MonthlyRate": st.number_input("Monthly Rate", min_value=1000, max_value=30000, value=15000),
    "NumCompaniesWorked": st.number_input("Num Companies Worked", min_value=0, max_value=10, value=3),
    "RelationshipSatisfaction": st.selectbox("Relationship Satisfaction", [1, 2, 3, 4]),
    "StockOptionLevel": st.selectbox("Stock Option Level", [0, 1, 2, 3]),
    "TotalWorkingYears": st.number_input("Total Working Years", min_value=0, max_value=50, value=10),
    "WorkLifeBalance": st.selectbox("Work-Life Balance", [1, 2, 3, 4]),
    "YearsAtCompany": st.number_input("Years at Company", min_value=0, max_value=40, value=5),
    "YearsInCurrentRole": st.number_input("Years in Current Role", min_value=0, max_value=20, value=3),
    "YearsSinceLastPromotion": st.number_input("Years Since Last Promotion", min_value=0, max_value=15, value=2),
    "YearsWithCurrManager": st.number_input("Years with Current Manager", min_value=0, max_value=20, value=3),
    "BusinessTravel_Travel_frequently": st.selectbox("Business Travel (Frequently)", [0, 1]),
    "MaritalStatus_Single": st.selectbox("Marital Status (Single)", [0, 1]),
    "OverTime_Yes": st.selectbox("Overtime (Yes)", [0, 1])
}

# Make prediction request
if st.button("Predict Attrition"):
    response = requests.post(API_URL, json=employee_data)
    if response.status_code == 200:
        result = response.json()
        st.write(f"**Attrition Probability:** {result['Attrition Probability']}")
        st.write(f"**Predicted Attrition:** {result['Predicted Attrition']}")
    else:
        st.error("Error: Could not fetch prediction. Ensure FastAPI server is running.")