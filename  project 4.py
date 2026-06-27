def student_database():
        students = {}

            while True:
                    print("\n1. Add Student")
                            print("2. Search Student")
                                    print("3. Display All Students")
                                            print("4. Exit")

                                                    choice = input("Enter Choice: ")

                                                            try:
                                                                        if choice == "1":
                                                                                        roll = int(input("Enter Roll No: "))
                                                                                                        name = input("Enter Name: ")
                                                                                                                        age = int(input("Enter Age: "))
                                                                                                                                        city = input("Enter City: ")

                                                                                                                                                        students.update({roll: {"Name": name, "Age": age, "City": city}})
                                                                                                                                                                        print("Student Added Successfully.")

                                                                                                                                                                                    elif choice == "2":
                                                                                                                                                                                                    roll = int(input("Enter Roll No to Search: "))
                                                                                                                                                                                                                    print(students.get(roll, "Student Not Found."))

                                                                                                                                                                                                                                elif choice == "3":
                                                                                                                                                                                                                                                if len(students) == 0:
                                                                                                                                                                                                                                                                    print("No Records Found.")
                                                                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                                                                                        for roll, details in students.items():
                                                                                                                                                                                                                                                                                                                                print(roll, details)

                                                                                                                                                                                                                                                                                                                                            elif choice == "4":
                                                                                                                                                                                                                                                                                                                                                            print("Program Ended.")
                                                                                                                                                                                                                                                                                                                                                                            break

                                                                                                                                                                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                                                                                                                                                                                        print("Invalid Choice.")

                                                                                                                                                                                                                                                                                                                                                                                                                except ValueError:
                                                                                                                                                                                                                                                                                                                                                                                                                            print("Invalid Input!")

                                                                                                                                                                                                                                                                                                                                                                                                                            student_database()
                                                                                                                                                                                                                                                                                                                                                                                                                            def