def manage_marks():
        marks = []

            try:
                    for i in range(5):
                                mark = float(input(f"Enter mark {i+1}: "))
                                            marks.append(mark)

                                                    print("\nMarks List:", marks)

                                                            average = sum(marks) / len(marks)

                                                                    print("Average =", average)
                                                                            print("Highest =", max(marks))
                                                                                    print("Lowest =", min(marks))

                                                                                            marks.sort(reverse=True)
                                                                                                    print("Descending Order =", marks)

                                                                                                        except ValueError:
                                                                                                                print("Please enter numeric values only.")

                                                                                                                manage_marks()