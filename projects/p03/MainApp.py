import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import streamlit as st


def loadData():
    file_path = "projects/p03/data_credit_score_classifier.csv"
    data = pd.read_csv(file_path)
    return data


def displayEDA(data):
    pass


def buildModel(data):
    # https://colab.research.google.com/drive/16yVdC2fyUO_J_6_jzyjFIrMda2TINC6Q?usp=sharing
    data["Credit_Mix"] = data["Credit_Mix"].map({"Standard": 1, "Good": 2, "Bad": 0})
    x = np.array(
        data[
            [
                "Annual_Income",
                "Monthly_Inhand_Salary",
                "Num_Bank_Accounts",
                "Num_Credit_Card",
                "Interest_Rate",
                "Num_of_Loan",
                "Delay_from_due_date",
                "Num_of_Delayed_Payment",
                "Credit_Mix",
                "Outstanding_Debt",
                "Credit_History_Age",
                "Monthly_Balance",
            ]
        ]
    )
    y = np.array(data[["Credit_Score"]])
    xtrain, xtest, ytrain, ytest = train_test_split(
        x, y, test_size=0.33, random_state=42
    )
    model = RandomForestClassifier()
    model.fit(xtrain, ytrain)
    return model


def loadPrebuiltModel():
    model_path = "projects/p03/cmodel_credit_score_classifier.joblib"
    model = joblib.load(model_path)
    return model


def App():
    # data = loadData()
    # displayEDA(data)
    model = loadPrebuiltModel()
    st.text("Credit Score Prediction : ")
    cols = st.columns(3)
    with cols[0]:
        anual_income = st.number_input(
            label="Anual Income",
            step=1000,
            value=90000
        )
        monthly_inhand_salary = st.number_input(
            label="Monthly Inhand Salary", step=1000, value=3000
        )
        monthly_balance = st.number_input(
            label="Month End balance", step=50, value=150
        )
        outstanding_debt = st.number_input(
            label="Outstanding Debt", step=50, value=2000
        )
        pass
    with cols[1]:
        no_of_bank_accounts = st.number_input(label="No of Bank Accounts", step=1, value=4)
        no_of_credit_cards = st.number_input(label="No of Credit Cards", step=1, value=3)
        interest_rates = st.number_input(label="Interest Rate", step=1.0, format="%.2f",value=1.5)
        no_of_loans = st.number_input(label="No of Loans", step=1,value=2)
        pass
    with cols[2]:
        avg_no_of_delay_days = st.number_input(
            label="Average Delay in Payments (Days)", step=1,value=10
        )
        no_of_delayed_paymets = st.number_input(label="No of Delayed Payments", step=1,value=5)
        credit_mix = st.number_input(label="Credit Mix", step=1, min_value=1, max_value=3,value=2)
        credit_history_age = st.number_input(
            label="Credit History Age", step=1.0, format="%.2f",value=600.0
        )
    if st.button("Classify Credit Score"):
        features = np.array(
            [
                [
                    anual_income,
                    monthly_inhand_salary,
                    no_of_bank_accounts,
                    no_of_credit_cards,
                    interest_rates,
                    no_of_loans,
                    avg_no_of_delay_days,
                    no_of_delayed_paymets,
                    credit_mix,
                    outstanding_debt,
                    credit_history_age,
                    monthly_balance,
                ]
            ]
        )
        st.write("Predicted Credit Score = ", model.predict(features))
    return
