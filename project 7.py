class Employee:
        def __init__(self, emp_id, name, details):
                self.emp_id = emp_id
                        self.name = name
                                self.details = details

                                    def show_details(self):
                                            print("Employee ID:", self.emp_id)
                                                    print("Name:", self.name)
                                                            print("Department:", self.details[0])
                                                                    print("Salary:", self.details[1])
                                                                            print()


                                                                            employees = {}

                                                                            for i in range(3):
                                                                                emp_id = int(input("Enter Employee ID: "))
                                                                                    name = input("Enter Name: ")
                                                                                        dept = input("Enter Department: ")
                                                                                            salary = float(input("Enter Salary: "))

                                                                                                employees[emp_id] = Employee(emp_id, name, (dept, salary))

                                                                                                print("\nEmployee Details")

                                                                                                for emp in employees.values():
                                                                                                    emp.show_details()