import streamlit as st
import numpy as np

# Calculator functions
def add(x, y): return np.add(x, y)
def subtract(x, y): return np.subtract(x, y)
def multiply(x, y): return np.multiply(x, y)
def divide(x, y): return np.divide(x, y)

# Web app layout
st.title("Simple Web Calculator")

x = st.number_input("Enter first number", value=0.0)
y = st.number_input("Enter second number", value=0.0)
operation = st.selectbox("Choose operation", ["Add", "Subtract", "Multiply", "Divide"])

if st.button("Calculate"):
    try:
        if operation == "Add":
            st.success(f"Result: {add(x, y)}")
        elif operation == "Subtract":
            st.success(f"Result: {subtract(x, y)}")
        elif operation == "Multiply":
            st.success(f"Result: {multiply(x, y)}")
        elif operation == "Divide":
            st.success(f"Result: {divide(x, y)}")
    except Exception as e:
        st.error(f"Error: {e}")
# This is a test file
# This file is used to test the ar.py file
