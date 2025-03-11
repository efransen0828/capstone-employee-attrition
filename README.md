﻿# Capstone Employee Attrition Project
## Overview

This repository contains the files and code for my Data Analytics Capstone Project at Western Governors University (WGU). The project focuses on analyzing and predicting employee attrition using machine learning techniques.

## Project Goals

The primary goal is to identify key predictors of employee attrition and develop a predictive model that can provide early warnings for at-risk employees, enabling organizations to implement proactive retention strategies.

## Dataset

Dataset Source: IBM HR Analytics Employee Attrition & Performance

Dataset Details:

- Employee demographics

- Job satisfaction and involvement

- Compensation data

- Performance metrics

- Work-life balance

## Repository Structure
capstone-employee-attrition/
├── app/                    # Application files
├── data/                   # Dataset (raw, processed, and visualizations)
│   ├── raw/                # Original raw data
│   ├── processed/          # Processed datasets for modeling
│   └── visualizations/     # Data visualizations (CSV outputs)
├── models/                 # Trained machine learning models and preprocessing objects
├── notebooks/              # Jupyter notebooks for exploratory data analysis and modeling
│   └── artifacts/          # Additional artifacts from notebooks (models, metadata)
├── results/                # Output visualizations and summary statistics
├── README.md               # Project documentation (this file)
└── requirements.txt        # Python dependencies

## Analytical Methods

The analysis process involved:
- Descriptive Analysis: Using statistical summaries and visualizations to uncover data patterns.
- Predictive Analysis: Training and evaluating machine learning models (Logistic Regression and Random Forest) to predict employee attrition.

## Key Tools & Technologies

- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn
- Jupyter Notebook
- Power BI
  
## Model Performance
The best-performing model, Logistic Regression, achieved:
- Accuracy: 87%
- Precision: 83%
- Recall: 88%
- F1-score: 85%
- AUC-ROC: 0.92

## How to Use This Repository

1. Clone the repository:
   git clone https://github.com/efransen0828/capstone-employee-attrition.git
2. Install dependencies:
   pip install -r requirements.txt
3. Navigate through notebooks to explore the analysis, modeling, and results:
   notebooks/employee_attrition_analysis.ipynb for exploratory analysis and predictive modeling.

## Author
Erika Fransen

## License
This project is provided for educational purposes.
   
