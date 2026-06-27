import random
import math

try:
    numbers = set()

        print("Enter 10 numbers:")

            for i in range(10):
                    numbers.add(int(input()))

                        print("Unique Numbers:", numbers)

                            t = tuple(numbers)
                                print("Tuple:", t)

                                    if len(t) >= 3:
                                            print("3 Random Numbers:", random.sample(t, 3))
                                                else:
                                                        print("Not enough unique numbers.")

                                                            total = sum(t)
                                                                print("Square Root of Sum =", math.sqrt(total))

                                                                except ValueError:
                                                                    print("Please enter valid integers.")

                                                                    except Exception as e:
                                                                        print("Error:", e)