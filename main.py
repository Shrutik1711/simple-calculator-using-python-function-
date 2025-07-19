def calculator():
    print("Welcome to the calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Addition")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Sum is: ", a + b)
    elif choice == 2:
        print("Subtraction")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Difference is: ", a - b)
    elif choice == 3:
        print("Multiplication")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Product is: ", a * b)
    elif choice == 4:
        print("Division")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Quotient is: ", a / b)
    elif choice == 5:
        print("Exiting")
        exit()
    else:
        print("Invalid choice")
calculator()  
