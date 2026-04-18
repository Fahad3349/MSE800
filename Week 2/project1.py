# Global variable to store student data
students_list = []

# Class definition
class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id

# Function to collect student data
def collect_student_data():
    for i in range(3):  # collect data for at least 3 students
        print(f"\nEnter details for Student {i + 1}")
        
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        student_id = input("Enter student ID: ")
        
        student = Student(name, age, student_id)
        students_list.append(student)  # using global variable

# Function to display sorted student data
def display_students():
    sorted_students = sorted(students_list, key=lambda x: x.age)
    
    print("\nStudent List (Sorted by Age):")
    for student in sorted_students:
        print(f"Name: {student.name}, Age: {student.age}")

# Entry point
if __name__ == "__main__":
    collect_student_data()
    display_students()
