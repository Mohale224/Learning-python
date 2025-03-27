class Student:
    def __init__(self, student_name, student_id):
        self.student_name = student_name
        self.student_id = student_id
        self.courses = []

    def enroll_course(self, course_name, grade):
        self.courses.append((course_name, grade))

    def display_details(self):
        print(f'Student Name: {self.student_name}')
        print(f'Student ID: {self.student_id}')
        print('Enrolled Courses:')
        for course in self.courses:
            print(f'{course[0]} : {course[1]}')


class StudentManagement:
    def __init__(self):
        self.students = []

    def add_student(self, student_name, student_id):
        new_student = Student(student_name, student_id)
        self.students.append(new_student)
        print(f'Student {student_name} with ID {student_id} added successfully.')

    def enroll_student(self, student_id, course_name, grade):
        for student in self.students:
            if student.student_id == student_id:
                student.enroll_course(course_name, grade)
                print(f'Student {student.student_name} enrolled in {course_name} with grade {grade}.')
                return
        print(f'Student with ID {student_id} not found.')

    def view_student_details(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                student.display_details()
                return
        print(f'Student with ID {student_id} not found.')

    def list_all_students(self):
        if not self.students:
            print("No students found.")
            return
        print("List of all students:")
        for student in self.students:
            print(f'Name: {student.student_name}, ID: {student.student_id}')


def main():
    sms = StudentManagement()+
    while True:
        print("\nStudent Management System")
        print("1. Add a new Student")
        print("2. Enroll a Student in a Course")
        print("3. View Student Details")
        print("4. List all Students")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            student_name = input("Enter Student Name: ")
            student_id = input("Enter Student ID: ")
            sms.add_student(student_name, student_id)

        elif choice == '2':
            student_id = input("Enter Student ID: ")
            course_name = input("Enter Course Name: ")
            grade = input("Enter Grade: ")
            sms.enroll_student(student_id, course_name, grade)

        elif choice == '3':
            student_id = input("Enter Student ID: ")
            sms.view_student_details(student_id)

        elif choice == '4':
            sms.list_all_students()

        elif choice == '5':
            print("Exiting program!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
