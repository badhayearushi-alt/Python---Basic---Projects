class Student:
        def __init__(self, name, roll_no):
                self.name = name
                        self.roll_no = roll_no
                                self.marks_list = []

                                    def add_mark(self, mark):
                                            if mark < 0 or mark > 100:
                                                        raise ValueError("Marks should be between 0 and 100.")
                                                                self.marks_list.append(mark)

                                                                    def get_average(self):
                                                                            if len(self.marks_list) == 0:
                                                                                        return 0
                                                                                                return sum(self.marks_list) / len(self.marks_list)

                                                                                                    def display_info(self):
                                                                                                            print("\nStudent Details")
                                                                                                                    print("Name:", self.name)
                                                                                                                            print("Roll No:", self.roll_no)
                                                                                                                                    print("Marks:", self.marks_list)
                                                                                                                                            print("Average:", self.get_average())


                                                                                                                                            try:
                                                                                                                                                name = input("Enter Name: ")
                                                                                                                                                    roll = int(input("Enter Roll No: "))

                                                                                                                                                        student = Student(name, roll)

                                                                                                                                                            for i in range(5):
                                                                                                                                                                    mark = float(input(f"Enter Mark {i+1}: "))
                                                                                                                                                                            student.add_mark(mark)

                                                                                                                                                                                student.display_info()

                                                                                                                                                                                except ValueError as e:
                                                                                                                                                                                    print("Error:", e)
                                                                                                                                                                                    class