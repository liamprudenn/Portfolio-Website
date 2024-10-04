while True:
    user_input = input("\n" + "Select Your Action: +, -, *, /, ^ or exit: ")
    if user_input == "exit" or user_input == "stop":
        print("exiting...")
        break

    for x in user_input:
        if x.isupper():
            user_input = user_input.lower()

        elif user_input not in (
            "-",
            "+",
            "*",
            "/",
            "^",
            "add",
            "subtract",
            "multiply",
            "divide",
            "power",
            "exit",
        ):
            print("Invalid input please try again")
        continue

    num1_input = input("Enter the first number or press enter for result): ")
    if num1_input == "exit" or num1_input == "stop":
        print("exiting...")
        break
    num1 = result if num1_input == "" else float(num1_input)

    num2_input = input("Enter the second number (or press Enter for result): ")
    if num1_input == "exit" or num1_input == "stop":
        print("exiting...")
        break

    num2 = result if num2_input == "" else float(num2_input)

    if user_input == "+" or user_input == "add":
        result = num1 + num2

    elif user_input == "-" or user_input == "subtract":
        result = num1 - num2

    elif user_input == "*" or user_input == "multiply":
        result = num1 * num2

    elif user_input == "/" or user_input == "divide":
        result = num1 / num2

    elif user_input == "^" or user_input == "power":
        result = 1
        for _ in range(int(num2)):
            result *= num1
    elif user_input == "remainder" or user_input == "%":
        result = num1%num2


    print("Total:", result)
