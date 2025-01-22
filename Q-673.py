class Student:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def putdata(self):
        print(f"Student Name: {self.name}, Email: {self.email}")

class PhDguide:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.students = []

    def putdata(self):
        print(f"Guide Name: {self.name}, Email: {self.email}")
        print("Students:")
        for student in self.students:
            student.putdata()

    def add(self, student):
        self.students.append(student)
        print(f"Added student: {student.name}")

    def remove(self, student):
        if student in self.students:
            self.students.remove(student)
            print(f"Removed student: {student.name}")
        else:
            print(f"Student {student.name} not found.")

guide = PhDguide("Dr. Smith", "smith@example.com")
student1 = Student("Alice", "alice@example.com")
student2 = Student("Bob", "bob@example.com")
guide.add(student1)
guide.add(student2)
guide.putdata()
guide.remove(student1)
guide.putdata()
