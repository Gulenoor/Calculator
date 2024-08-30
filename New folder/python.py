import streamlit as st

# Function to perform calculations
def calculate(operation, num1, num2):
    if operation == "Addition":
        return num1 + num2
    elif operation == "Subtraction":
        return num1 - num2
    elif operation == "Multiplication":
        return num1 * num2
    elif operation == "Division":
        return num1 / num2 if num2 != 0 else "Error: Division by zero"
    elif operation == "Percentage":
        return (num1 * num2) / 100

# Streamlit UI
st.title("Simple Calculator")

# Input fields
num1 = st.number_input("Enter the first number", value=0.0)
num2 = st.number_input("Enter the second number", value=0.0)
operation = st.selectbox("Select operation", ["Addition", "Subtraction", "Multiplication", "Division", "Percentage"])

# Calculate and display result
if st.button("Calculate"):
    result = calculate(operation, num1, num2)
    st.write(f"The result of {operation} is: {result}")
