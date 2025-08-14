# Basic Calculator Program


num1 = float(input("Enter the first number: "))

num2 = float(input("Enter the second number: "))


operation = input("Enter the operation (+, -, *, /): ")

# Perform the operation based on user input
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero is not allowed."
else:
    result = "Invalid operation!"

# Display the result
if isinstance(result, (int, float)):
    print(f"{num1} {operation} {num2} = {result}")
else:
    print(result)
