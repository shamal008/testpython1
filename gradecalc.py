class Student:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

def calculate_grade(mark):
    if mark >= 90:
        print("Grade: A")
    elif mark >= 75:
        print("Grade: B")
    elif mark >= 50:    
        print("Grade: C")
    else:
        print("Grade: Fail")

student1 = Student("kaduva", 85)
print(student1.name, student1.mark)
calculate_grade(student1.mark)

student2 = Student("Shifin", 45)            
print(student2.name, student2.mark)
calculate_grade(student2.mark)
