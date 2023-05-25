import pickle
import numpy as np
import pandas as pd
import streamlit as st

model = pickle.load(open("model.pkl", "rb"))

def find_type(text):
	if text == "CASH_IN":
		return 0
	elif text == "CASH_OUT":
		return 1
	elif text == "DEBIT":
		return 2
	elif text == "PAYMENT":
		return 3
	else:
		return 4

st.title("Online Payments Fraud Detection")
types = st.selectbox("Type", ("CASH_IN", "CASH_OUT", "DEBIT", "PAYMENT", "TRANSFER"))
amount = st.number_input("Amount")
oldbalanceOrg = st.number_input("Old Balance Original")
newbalanceOrg = st.number_input("New Balance Original")

if st.button("Predict"):
	types = find_type(types)
	test = np.array([[types, amount, oldbalanceOrg, newbalanceOrg]])
	res = model.predict(test)
	print(res)
	st.success("Prediction: " + str(res[0]))
