from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

# Load trained model
model_path = "C:/Users/efran/capstone-employee-attrition/notebooks/best_rf_model.pkl"
model = joblib.load(model_path)

# Define input schema for request validation
class EmployeeFeatures(BaseModel):
    Age: float
    DailyRate: float
    DistanceFromHome: float
    Education: int
    EmployeeNumber: int
    EnvironmentSatisfaction: int
    HourlyRate: float
    JobInvolvement: int
    JobSatisfaction: int
    MonthlyIncome: float
    MonthlyRate: float
    NumCompaniesWorked: int
    PercentSalaryHike: int
    PerformanceRating: int
    RelationshipSatisfaction: int
    StockOptionLevel: int
    TotalWorkingYears: int
    TrainingTimesLastYear: int
    WorkLifeBalance: int
    YearsAtCompany: int
    YearsSinceLastPromotion: int
    BusinessTravel_Travel_frequently: int
    BusinessTravel_Travel_rarely: int
    Department_Research_and_development: int
    Department_Sales: int
    EducationField_Life_sciences: int
    EducationField_Marketing: int
    EducationField_Medical: int
    EducationField_Other: int
    EducationField_Technical_degree: int
    Gender_Male: int
    JobRole_Human_resources: int
    JobRole_Laboratory_technician: int
    JobRole_Manager: int
    JobRole_Manufacturing_director: int
    JobRole_Research_director: int
    JobRole_Research_scientist: int
    JobRole_Sales_representative: int
    MaritalStatus_Married: int
    MaritalStatus_Single: int
    OverTime_Yes: int
    OverTime_JobSatisfaction: int

# **NEW: Correct field names before prediction**
column_mapping = {
    "Department_Research_and_development": "Department_Research & development",
    "EducationField_Life_sciences": "EducationField_Life sciences",
    "EducationField_Technical_degree": "EducationField_Technical degree",
    "JobRole_Human_resources": "JobRole_Human resources",
    "JobRole_Laboratory_technician": "JobRole_Laboratory technician",
    "JobRole_Manufacturing_director": "JobRole_Manufacturing director",
    "JobRole_Research_director": "JobRole_Research director",
    "JobRole_Research_scientist": "JobRole_Research scientist",
    "JobRole_Sales_representative": "JobRole_Sales representative",
}

@app.post("/predict")
def predict(employee: EmployeeFeatures):
    # Convert input to dictionary
    employee_dict = employee.dict()

    # **NEW: Rename fields to match model**
    corrected_input = {
        column_mapping.get(k, k): v for k, v in employee_dict.items()
    }

    # Convert to DataFrame
    input_df = pd.DataFrame([corrected_input])

    # Ensure columns match model
    input_df = input_df[model.feature_names_in_]

    # Make prediction
    prediction = model.predict(input_df)

    return {"prediction": int(prediction[0])}
