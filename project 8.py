import math

try:
    sentence = input("Enter a sentence: ")

        words = set(sentence.split())

            print("\nUnique Words (Sorted):")
                for word in sorted(words):
                        print(word)

                            total = len(words)

                                print("\nTotal Unique Words =", total)
                                    print("Power of 2 =", math.pow(total, 2))

                                    except Exception as e:
                                        print("Error:", e)