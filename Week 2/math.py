import math

# Function 1: Basic operations
def basic_operations(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    elif operator == '%':
        return a % b
    else:
        return "Invalid operator"


# Function 2: Factorial
def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    return math.factorial(n)


# Function 3: Complex number operations
def complex_operations(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operator"


# Main program
def main():
    print(" Calculate ")
    print("1. Basic Operations")
    print("2. Factorial")
    print("3. Complex Number Operations")

    choice = input("Choose an option (1/2/3): ")

    if choice == '1':
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        op = input("Enter operator (+, -, *, /, %): ")
        print("Result:", basic_operations(a, b, op))

    elif choice == '2':
        n = int(input("Enter a number: "))
        print("Factorial:", factorial(n))

    elif choice == '3':
        print("Enter complex numbers (e.g., 2+3j)")
        a = complex(input("Enter first complex number: "))
        b = complex(input("Enter second complex number: "))
        op = input("Enter operator (+, -, *, /): ")
        print("Result:", complex_operations(a, b, op))

    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()