def add_numbers(a, b):
    return a + b

if __name__ == "__main__":

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Sum:", add_numbers(num1, num2))
    except ValueError:
        print("Error: Please enter numbers only!")

