class Student:
    def __init__(self,student_name,student_id,courses):
        self.student_name = student_name
        self.student_id = student_id
        self.courses = courses

        def __init__(self):
            self.courses_id = {}
            self.display_details = {}
        def enroll_course(self,course_id,grade):
            if course_id not in self.courses_id:
                self.courses_id[course_id] = (grade)  
                print("Course enrolled successfully.")
            else:
                print