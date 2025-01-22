class StudentCompare:
    def __init__(self, roll_no, name, age, total_marks):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.total_marks = total_marks

    def __eq__(self, other):
        return self.total_marks == other.total_marks

# Example usage
student1 = StudentCompare(1, "Alice", 20, 85)
student3 = StudentCompare(3, "Charlie", 22, 90)
print(tudent1 == student3)
