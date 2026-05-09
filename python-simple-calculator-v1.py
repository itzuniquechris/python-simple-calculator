while True:
    print("\n--- Simple Calculator ---")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    option = input("\nSelect an option (1-5): ")

    if not option.isdigit():
        print(f"'{option}' is not a valid choice!")
        print("Please enter a number between 1 and 5.")
        continue

    if option == "5":
        print("Exiting calculator. Goodbye!")
        print("\n[Program Finished]")
        break

    if option in ("1", "2", "3", "4"):
        num1 = float(input("\nEnter first number: "))
        num2 = float(input("Enter second number: "))

        if option == "1":
            result = num1 + num2
            print(f"Result: {num1:.2f} + {num2:.2f} = {result:.2f}")
        
        elif option == "2":
            result = num1 - num2
            print(f"Result: {num1:.2f} - {num2:.2f} = {result:.2f}")
        
        elif option == "3":
            result = num1 * num2
            print(f"Result: {num1:.2f} * {num2:.2f} = {result:.2f}")
        
        elif option == "4":
            if num2 == 0:
                print("Error: Cannot Divide by Zero!")
                continue
            result = num1 / num2
            print(f"Result: {num1:.2f} / {num2:.2f} = {result:.2f}")
    else:
        print("Invalid choice! Please select a number between 1 and 5.")
