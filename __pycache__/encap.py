class Employee:
    def __init__(self, name, salary):
        self.__name = name  # Private attribute
        self.__salary = salary  # Private attribute

    def display_info(self):
        print(f"Name: {self.__name}, Salary: {self.__salary}")

    # def update_salary(self, new_salary):
    #     self.__salary = new_salary

emp = Employee("Shamal", 150000)
emp.display_info()

# emp.update_salary(20000)
# emp.display_info()