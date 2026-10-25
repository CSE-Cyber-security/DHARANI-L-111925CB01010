"""Simple Calculator - performs addition, subtraction, multiplication and division."""


def get_number(prompt):
    """Keep asking until the user enters a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Invalid numeric input.")


def fmt(n):
    """Show whole numbers without the trailing .0"""
    return int(n) if n == int(n) else round(n, 4)


def calculator():
    while True:
        print("\n=== Simple Calculator ===")
        choice = input("Select an operation (1/2/3/4) or 'q' to quit:\n"
                       "  1. Addition\n  2. Subtraction\n"
                       "  3. Multiplication\n  4. Division\n"
                       "Enter choice: ").strip().lower()

        if choice == "q":
            print("Thank you! Goodbye!")
            break
        if choice not in ("1", "2", "3", "4"):
            print("Error: Please choose 1, 2, 3, 4 or 'q'.")
            continue

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        if choice == "1":
            print(f"Result: {fmt(num1)} + {fmt(num2)} = {fmt(num1 + num2)}")
        elif choice == "2":
            print(f"Result: {fmt(num1)} - {fmt(num2)} = {fmt(num1 - num2)}")
        elif choice == "3":
            print(f"Result: {fmt(num1)} * {fmt(num2)} = {fmt(num1 * num2)}")
        else:
            while num2 == 0:
                print("Error: Cannot divide by zero.")
                num2 = get_number("Enter second number: ")
            print(f"Result: {fmt(num1)} / {fmt(num2)} = {fmt(num1 / num2)}")


if __name__ == "__main__":
    calculator()
