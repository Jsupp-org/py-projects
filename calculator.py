print("\n=== Calculator ===")

while True:
    # Getting the user input for two numbers
    num1 = float(input("\nEnter first number: "))
    sign = input("Enter operation (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    # Performing calculations based on the operator entered by the user
    if sign == "+":
        result = num1 + num2
        print("\nResult:", result)
    elif sign == "-":
        result = num1 - num2
        print("\nResult:", result)
    elif sign == "*":
        result = num1*num2
        print("\nResult:", result)
    elif sign == "/":
        if num2 != 0:
            result = num1/num2
            print("\nResult:", result)
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation. Please enter a valid operator. Thank you!")

    # Asking the user if they want to perform another calculation
    choice = input("\nDo you want to perform another calculation? (yes/no): ")
    if choice.lower() == "no":
        print("\nThank you for using the calculator. Goodbye!")
        break
    
