from math import *


class calc:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Error: Division by zero!"
        else:
            return x / y

    def sin(self, x):
        return sin(x)

    def cos(self, x):
        return cos(x)

    def tan(self, x):
        return tan(x)

    def log(self, x, y):
        return log(self, x, y)

    def exp(self, x):
        return exp(x)


def main():
    calculator = calc()
    print("Welcome to Calculator!!!")

    while True:
        print("\nOperations:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Sin")
        print("6. Cos")
        print("7. Tan")
        print("8. Logarithm")
        print("9. Exponential")
        print("10. Quit")

        choice = input("Enter your choice (1-10): ")

        if choice == "10":
            print("Thank you for using Calculator App!")
            break

        elif choice in ["1", "2", "3", "4"]:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == "1":
                print("You picked: Addition")
                print("Result:", calculator.add(num1, num2))
            elif choice == "2":
                print("You picked: Subtract")
                print("Result:", calculator.subtract(num1, num2))
            elif choice == "3":
                print("You picked: Multiplication")
                print("Result:", calculator.multiply(num1, num2))
            elif choice == "4":
                print("You picked: vision")
                print("Result:", calculator.divide(num1, num2))

        elif choice in ["5", "6", "7"]:
            angle = float(input("Enter angle in degrees: "))

            if choice == "5":
                print("You picked: Sine")
                print("Result:", calculator.sin(angle))
            elif choice == "6":
                print("You picked: Cosine")
                print("Result:", calculator.cos(angle))
            elif choice == "7":
                print("You picked: Tan")
                print("Result:", calculator.tan(angle))

        elif choice == "8":
            num = float(input("Enter number: "))
            base = float(input("Enter base: "))
            print("Result:", calculator.log(num, base))
        elif choice == "9":
            num = float(input("Enter number: "))
            print("Result:", calculator.exp(num))

        else:
            print("Invalid choice. Please enter a number between 1 and 10.")


if __name__ == "__main__":
    main()
