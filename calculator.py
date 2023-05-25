import streamlit as st

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

# Streamlit app code
st.title("Calculator")

# Input fields for numbers
number1 = st.number_input("Enter the first number", value=0.0)
number2 = st.number_input("Enter the second number", value=0.0)

# Button for addition
if st.button("Add"):
    result = add(number1, number2)
    st.write("Result:", result)

# Button for subtraction
if st.button("Subtract"):
    result = subtract(number1, number2)
    st.write("Result:", result)

# Button for multiplication
if st.button("Multiply"):
    result = multiply(number1, number2)
    st.write("Result:", result)

# Button for division
if st.button("Divide"):
    result = divide(number1, number2)
    st.write("Result:", result)
