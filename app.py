import streamlit as st

def main():
    st.title("Calculator")

    num1 = st.number_input("Enter the first number:")
    num2 = st.number_input("Enter the second number:")

    operation = st.selectbox(
        "Select an operation",
        ("Addition", "Subtraction", "Multiplication", "Division")
    )

    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"

    st.write("Result:", result)

if __name__ == "__main__":
    main()