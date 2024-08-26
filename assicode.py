class StudentDatabase:
    def __init__(self):
        self.students = {}

    def add_student(self, student):
        self.students[student.id] = student

    def remove_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]

    def get_student(self, student_id):
        return self.students.get(student_id)

    def get_all_students(self):
        return self.students.values()

class Student:
    def __init__(self, id, name, age, major):
        self.id = id
        self.name = name
        self.age = age
        self.major = major

    def update_info(self, name=None, age=None, major=None):
        if name:
            self.name = name
        if age:
            self.age = age
        if major:
            self.major = major

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Age: {self.age}, Major: {self.major}"

class StudentManagementSystem:
    def __init__(self, database: StudentDatabase):
        self.database = database

    def add_new_student(self, id, name, age, major):
        student = Student(id, name, age, major)
        self.database.add_student(student)

    def delete_student(self, student_id):
        self.database.remove_student(student_id)

    def update_student_info(self, student_id, name=None, age=None, major=None):
        student = self.database.get_student(student_id)
        if student:
            student.update_info(name, age, major)

    def show_all_students(self):
        students = self.database.get_all_students()
        for student in students:
            print(student)

class Menu:
    def __init__(self, system: StudentManagementSystem):
        self.system = system

    def display_menu(self):
        while True:
            print("\n1. Add Student")
            print("2. Delete Student")
            print("3. Update Student Information")
            print("4. View All Students")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.delete_student()
            elif choice == '3':
                self.update_student()
            elif choice == '4':
                self.view_students()
            elif choice == '5':
                print("Exiting the system.")
                break
            else:
                print("Invalid choice. Please try again.")

    def add_student(self):
        id = int(input("Enter Student ID: "))
        name = input("Enter Student Name: ")
        age = int(input("Enter Student Age: "))
        major = input("Enter Student Major: ")
        self.system.add_new_student(id, name, age, major)

    def delete_student(self):
        student_id = int(input("Enter Student ID to delete: "))
        self.system.delete_student(student_id)

    def update_student(self):
        student_id = int(input("Enter Student ID to update: "))
        name = input("Enter new name (leave blank to keep current): ")
        age = input("Enter new age (leave blank to keep current): ")
        major = input("Enter new major (leave blank to keep current): ")
        self.system.update_student_info(student_id, name or None, int(age) if age else None, major or None)

    def view_students(self):
        self.system.show_all_students()
        