<151115>_q2.py

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.assignments = {}

    def add_assignment(self, assignment_name, grade):
        self.assignments[assignment_name] = grade
        print(f"Added {assignment_name} for {self.name} with grade {grade}.")

    def display_grades(self):
        print(f"{self.name}'s Grades:")
        for assignment, grade in self.assignments.items():
            print(f"{assignment}: {grade}")

class Instructor:
    def __init__(self, name, course_name):
        self.name = name
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"{student.name} added to {self.course_name}.")

    def assign_grade(self, student, assignment_name, grade):
        student.add_assignment(assignment_name, grade)

    def display_all_students_grades(self):
        print(f"Grades for {self.course_name}:")
        for student in self.students:
            student.display_grades()

# Interactive example
instructor = Instructor("Dr. Brown", "Intro to Python")
student1 = Student("John", "S001")
student2 = Student("Emma", "S002")

instructor.add_student(student1)
instructor.add_student(student2)
instructor.assign_grade(student1, "Assignment 1", 85)
instructor.assign_grade(student2, "Assignment 1", 90)
instructor.display_all_students_grades()
