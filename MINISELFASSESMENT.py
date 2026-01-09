USERNAME = input("Enter your name :").strip().title()
print(f"WELCOME!!! {USERNAME}")
choice = int(input("Enter your choice (1-5): "))


if choice == 1:
    print("Weight Converter selected")
    if choice == 1:
        weight = float(input("Enter the weight: "))
        unit = input("Enter unit (kg/lbs): ").lower()

        if unit == "kg":
            lbs = weight * 2.205
            print(f"{weight} Kg = {lbs:.2f} Lbs")

        elif unit == "lbs":
            kg = weight / 2.205
            print(f"{weight} Lbs = {kg:.2f} Kg")

        else:
            print("Invalid unit. Please enter kg or lbs.")


elif choice == 2:
    temp = float(input("Enter temperature: "))
    unit = input("Enter unit (C/F): ").lower()

    if unit == "c":
        f = (temp * 9/5) + 32
        print(f"{temp}°C = {f:.2f}°F")

    elif unit == "f":
        c = (temp - 32) * 5/9
        print(f"{temp}°F = {c:.2f}°C")

    else:
        print("Invalid unit. Please enter C or F.")


elif choice == 3:
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operator == "+":
        print(f"Result: {num1 + num2}")

    elif operator == "-":
        print(f"Result: {num1 - num2}")

    elif operator == "*":
        print(f"Result: {num1 * num2}")

    elif operator == "/":
        if num2 != 0:   # logical check
            print(f"Result: {num1 / num2}")
        else:
            print("Error: Division by zero is not allowed")

    else:
        print("Invalid operator")


elif choice == 4:
    temp = float(input("Enter current temperature: "))

    message = (
        "Cold weather  " if temp < 20
        else "Normal weather ️" if temp <= 30
        else "Hot weather "
    )

    print(message)


elif choice == 5:
    noun = input("Enter a noun: ").lower()
    verb = input("Enter a verb: ").lower()
    place = input("Enter a place: ").title()

    print("\n--- Mad Libs Story ---")
    print(f"One day, a {noun} decided to {verb} at {place}. Everyone was surprised!")


else:
    print("Invalid choice. Please select between 1 and 5.")