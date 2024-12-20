# Write a Python class named Student with two attributes student_name, marks. Modify the attribute values of the said 
# class and print the original and modified values of the said attributes.

class Student:
    def __init__(self, student_name, marks):
        self.student_name = student_name
        self.marks = marks

    def display_original_values(self):
        print("Name:", self.student_name)
        print("Marks:", self.marks)

    def modify_values(self, new_name, new_marks):
        print("\nUpdating values...")
        self.student_name = new_name
        self.marks = new_marks

    def display_modified_values(self):
        print("Name:", self.student_name)
        print("Marks:", self.marks)


student = Student("John", 85)

print("Original Values:")
student.display_original_values()

student.modify_values("Emma", 95)

print("\nModified Values:")
student.display_modified_values()
