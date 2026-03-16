# Credit Risk Prediction Project

## Overview

This project analyzes and predicts **credit default risk** using machine learning techniques. The workflow includes data cleaning, exploratory data analysis (EDA), and predictive modeling to identify patterns related to credit risk.

The goal of the project is to build a model that helps financial institutions assess whether a borrower is likely to **default on a loan** based on financial and demographic features.

---

# Project Structure

```
credit_risk_project/
│
├── README.md
│
├── data/
│   ├── credit_risk_dataset.csv      # Raw dataset
│   └── data_clean.csv               # Cleaned dataset used for modeling
│
├── notebooks/
│   ├── Clean_data.ipynb             # Data cleaning and preprocessing
│   ├── Visualization.ipynb          # Exploratory Data Analysis (EDA)
│   └── modeling.ipynb               # Model training and evaluation
│
├── assets/
│   ├── eda_distribution.png
│   ├── eda_correlation.png
│   ├── eda_feature_analysis.png
│   └── model_results.png
│
└── src/
```

---

# Notebooks

## 1. Clean_data.ipynb

This notebook performs the **data preprocessing pipeline**, including:

* Loading the dataset
* Inspecting missing values
* Handling missing data
* Feature engineering
* Data cleaning and transformation
* Exporting the processed dataset

Output:

```
data/data_clean.csv
```

Example preprocessing result:

![Data Cleaning](./assets/screenshots/cleandata1.PNG)

---

## 2. Visualization.ipynb

This notebook focuses on **Exploratory Data Analysis (EDA)** to understand the dataset and identify patterns related to credit risk.

Key steps include:

* Statistical summaries
* Feature distribution analysis
* Credit risk comparison across variables
* Correlation analysis
* Data visualization

Example visualizations:

![Feature Distribution](./assets/screenshots/output.png)

![Correlation Matrix](./assets/screenshots/output2.png)
![Correlation Matrix](./assets/screenshots/output3.png)

---

## 3. modeling.ipynb

This notebook builds and evaluates **machine learning models** for predicting credit default.

Steps include:

* Data preparation
* Train/Test split
* Model training
* Model evaluation
* Performance metrics
* Feature importance analysis

Example model results:

![Model Results](./assets/screenshots/Capture.PNG)

---

# Dataset

### credit_risk_dataset.csv

The original dataset containing borrower information such as:

* Income
* Loan amount
* Loan status
* Employment details
* Credit history
* Other financial indicators

### data_clean.csv

The cleaned dataset generated after preprocessing, ready for modeling.

---

# Technologies Used

* Python 3.10
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Jupyter Notebook

---

# Getting Started

## 1. Clone the repository

```
git clone https://github.com/your-username/credit_risk_project.git
cd credit_risk_project
```

---

## 2. Install system dependencies

```
sudo apt update
sudo apt install libpq-dev gcc python3-dev
```

---

## 3. Install Miniconda

Download and install **Miniconda** from:

https://docs.anaconda.com/free/miniconda/#quick-command-line-install

---

## 4. Create a Python environment

```
conda create -n credit-risk python=3.10
```

Activate the environment:

```
conda activate credit-risk
```

---

## 5. Install Python dependencies

```
pip install -r requirements.txt
```

---

# Running the Project

Run the notebooks in the following order:

1️⃣ Clean_data.ipynb
2️⃣ Visualization.ipynb
3️⃣ modeling.ipynb

This ensures the correct workflow from **data preprocessing → EDA → modeling**.

---

# Optional: Run FastAPI Server (Development Mode)

If the project includes an API for model inference, you can run it using:

```
uvicorn main:app --reload --port 5000
```

The API will be available at:

```
http://127.0.0.1:5000
```

---

# Project Goals

* Understand financial risk patterns
* Explore relationships between borrower features and loan default
* Build a machine learning model for credit risk prediction
* Demonstrate a complete **Data Science workflow**

---

# Future Improvements

* Add advanced feature engineering
* Perform hyperparameter tuning
* Implement additional machine learning models
* Deploy the model as a production API
* Build an interactive dashboard for risk analysis
