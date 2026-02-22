"""
Simple Calculator Application
Supports:
- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)
- BODMAS using expression evaluation
Handles:
- Invalid inputs
- Division by zero
"""

def calculate(expression):
    try:
        # Replace user-friendly symbols if needed
        expression = expression.replace("×", "*").replace("÷", "/")

        # Evaluate the mathematical expression (BODMAS supported)
        result = eval(expression)

        return result

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    except Exception:
        return "Error: Invalid input."


def main():
    print("🧮 Simple Calculator")
    print("Supported operators: +, -, *, /")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("Enter expression: ")

        if user_input.lower() == "exit":
            print("Calculator closed.")
            break

        result = calculate(user_input)
        print("Result:", result)
        print()


if __name__ == "__main__":
    main()