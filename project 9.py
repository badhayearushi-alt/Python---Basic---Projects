import math
import random
from datetime import datetime

history = {}

while True:
    print("\n----- Smart Calculator & Data Manager -----")
        print("1. Basic Arithmetic")
            print("2. Scientific Calculations")
                print("3. Generate Random Number")
                    print("4. View History")
                        print("5. Exit")

                            choice = input("Enter Choice: ")

                                if choice == "1":
                                        try:
                                                    a = float(input("Enter First Number: "))
                                                                b = float(input("Enter Second Number: "))

                                                                            print("1.Add 2.Subtract 3.Multiply 4.Divide")
                                                                                        op = input("Choose Operation: ")

                                                                                                    if op == "1":
                                                                                                                    result = a + b
                                                                                                                                elif op == "2":
                                                                                                                                                result = a - b
                                                                                                                                                            elif op == "3":
                                                                                                                                                                            result = a * b
                                                                                                                                                                                        elif op == "4":
                                                                                                                                                                                                        result = a / b
                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                    print("Invalid Operation")
                                                                                                                                                                                                                                                    continue

                                                                                                                                                                                                                                                                print("Result =", result)
                                                                                                                                                                                                                                                                            history[str(datetime.now())] = result

                                                                                                                                                                                                                                                                                    except ZeroDivisionError:
                                                                                                                                                                                                                                                                                                print("Cannot divide by zero.")
                                                                                                                                                                                                                                                                                                        except ValueError:
                                                                                                                                                                                                                                                                                                                    print("Invalid Input.")

                                                                                                                                                                                                                                                                                                                        elif choice == "2":
                                                                                                                                                                                                                                                                                                                                num = float(input("Enter Number: "))
                                                                                                                                                                                                                                                                                                                                        result = math.sqrt(num)
                                                                                                                                                                                                                                                                                                                                                print("Square Root =", result)
                                                                                                                                                                                                                                                                                                                                                        history[str(datetime.now())] = result

                                                                                                                                                                                                                                                                                                                                                            elif choice == "3":
                                                                                                                                                                                                                                                                                                                                                                    r = random.randint(1, 100)
                                                                                                                                                                                                                                                                                                                                                                            print("Random Number =", r)
                                                                                                                                                                                                                                                                                                                                                                                    history[str(datetime.now())] = r

                                                                                                                                                                                                                                                                                                                                                                                        elif choice == "4":
                                                                                                                                                                                                                                                                                                                                                                                                print("\nHistory")
                                                                                                                                                                                                                                                                                                                                                                                                        if not history:
                                                                                                                                                                                                                                                                                                                                                                                                                    print("No Records Found.")
                                                                                                                                                                                                                                                                                                                                                                                                                            else:
                                                                                                                                                                                                                                                                                                                                                                                                                                        for t, v in history.items():
                                                                                                                                                                                                                                                                                                                                                                                                                                                        print(t, ":", v)

                                                                                                                                                                                                                                                                                                                                                                                                                                                            elif choice == "5":
                                                                                                                                                                                                                                                                                                                                                                                                                                                                    print("Program Ended.")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                            break

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                else:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        print("Invalid Choice.")