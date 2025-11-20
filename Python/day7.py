# caluculator app
class caluculator:
    def addition(self, a, b):
        c = a + b
        return c

    def substraction(self, a, b):
        c = a - b
        return c

    def multiplication(self, a, b):
        c = a * b
        return c

    def division(self, a, b):
        if b == 0:
            return f"can not be divided"
        else:
            c = a / b
            return c

    def remainder(self, a, b):
        if b == 0:
            return f"can not be divided"
        else:
            c = a % b
            return c

    def quotient(self, a, b):
        if b == 0:
            return f"can not be divided"
        else:
            c = a // b
            return c

    def power(self, a, b):
        c = a ** b
        return c


def main():
    c = caluculator()
    while True:
        print("\nAvailable operation in the calculator are:")
        print("Enter 1 for additon.")
        print("Enter 2 for substraction.")
        print("Enter 3 for multiplication.")
        print("Enter 4 for division.")
        print("Enter 5 for remainder.")
        print("Enter 6 for quotient.")
        print("Enter 7 for power.")
        print("Enter 8 for exit.")
        try:
            choice = int(input("Enter your choice of operation:"))
        except:
            print(" Invalid choice !.Enter your choice from 1 to 8.")
            continue

        if choice == 8:
            print("Successfully existed.")
            break
        if 1 > choice or choice > 8:
            print("Invalid choice")
            continue

        while True:
            try:
                x = float(input("Enter the first number:"))
                y = float(input("Enter the second number:"))
                break

            except:
                print("Enter float values only:")
                continue

        if choice == 1:
            print(
                f"Anwser after addition is: {c.addition(x, y)}")
        elif choice == 2:
            print(
                f"Anwser after substraction is: {c.substraction(x, y)}")
        elif choice == 3:
            print(
                f"Anwser after multiplication is: {c.multiplication(x, y)}")
        elif choice == 4:
            print(
                f"Anwser after division is: {c.division(x, y)}")
        elif choice == 5:
            print(
                f"Anwser for remainder is: {c.remainder(x, y)}")
        elif choice == 6:
            print(
                f"Anwser for quotient is: {c.quotient(x, y)}")
        elif choice == 7:
            print(
                f"Anwser after powering is: {c.power(x, y)}")
        d = input("Do you want to continue (yes/no).").strip().lower()
        if d in ("yes", "y"):
            print("Continuing operation.")
            continue
        else:
            print("Existing caluculator.")
            break


if __name__ == "__main__":
    main()


print("*" * 50)

# Simplified


class Calculator:
    def addition(self, a, b): return a + b
    def subtraction(self, a, b): return a - b
    def multiplication(self, a, b): return a * b

    def division(
        self, a, b): return "Cannot divide by zero" if b == 0 else a / b

    def remainder(
        self, a, b): return "Cannot divide by zero" if b == 0 else a % b
    def quotient(
        self, a, b): return "Cannot divide by zero" if b == 0 else a // b

    def power(self, a, b): return a ** b


def main():
    calc = Calculator()
    operations = {
        1: ("Addition", calc.addition),
        2: ("Subtraction", calc.subtraction),
        3: ("Multiplication", calc.multiplication),
        4: ("Division", calc.division),
        5: ("Remainder", calc.remainder),
        6: ("Quotient", calc.quotient),
        7: ("Power", calc.power),
    }

    while True:
        print("\nAvailable operations:")
        for key, (name, _) in operations.items():
            print(f"Enter {key} for {name}.")
        print("Enter 8 to Exit.")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice! Enter numbers only (1–8).")
            continue

        if choice == 8:
            print("✅ Successfully exited.")
            break

        if choice not in operations:
            print("❌ Invalid choice. Please try again.")
            continue

        try:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
        except ValueError:
            print("❌ Invalid input! Enter numbers only.")
            continue

        op_name, func = operations[choice]
        print(f"👉 Answer after {op_name} is: {func(x, y)}")

        d = input("Do you want to continue (yes/no)? ").strip().lower()
        if d not in ("yes", "y"):
            print("👋 Exiting calculator.")
            break


if __name__ == "__main__":
    main()
