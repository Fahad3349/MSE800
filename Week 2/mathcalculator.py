import math

# CLASS
class Calculator:

    # Method 1: Addition
    def add(self, a, b):
        return a + b

    # Method 2: Subtraction
    def subtract(self, a, b):
        return a - b

    # Method 3: Multiplication
    def multiply(self, a, b):
        return a * b

    # Method 4: Division
    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b

    # Method 5: Modulus
    def modulus(self, a, b):
        return a % b

    # Method 6: Factorial
    def factorial(self, n):
        if n < 0:
            return "Error: Negative number"
        return math.factorial(n)

    # Method 7: Complex number addition
    def complex_add(self, c1, c2):
        return c1 + c2


# ---------------- FUNCTIONS (Outside Class) ----------------

def get_number_input():
    return float(input("Enter number: "))


def menu():
    print("\n===== CALCULATOR MENU =====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Factorial")
    print("7. Complex Addition")
    print("0. Exit")


# ---------------- MAIN PROGRAM ----------------
calc = Calculator()

while True:
    menu()
    choice = input("Choose option: ")

    if choice == "1":
        print(calc.add(get_number_input(), get_number_input()))

    elif choice == "2":
        print(calc.subtract(get_number_input(), get_number_input()))

    elif choice == "3":
        print(calc.multiply(get_number_input(), get_number_input()))

    elif choice == "4":
        print(calc.divide(get_number_input(), get_number_input()))

    elif choice == "5":
        print(calc.modulus(get_number_input(), get_number_input()))

    elif choice == "6":
        n = int(input("Enter integer: "))
        print(calc.factorial(n))

    elif choice == "7":
        a = complex(input("Enter first complex number (e.g. 2+3j): "))
        b = complex(input("Enter second complex number: "))
        print(calc.complex_add(a, b))

    elif choice == "0":
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")