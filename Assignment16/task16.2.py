class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []

    def describe_student(self):
        print("Student Information:")
        print("Name:", self.name)
        print("Student ID:", self.student_id)
        print("Courses:", self.courses if self.courses else "No courses registered")

    def describe_courses(self):
        if self.courses:
            print("Courses Registered for", self.name + ":")
            for course in self.courses:
                print("-", course)
        else:
            print(self.name, "is not registered for any courses.")

    def register_course(self, course):
        self.courses.append(course)
        print(self.name, "has successfully registered for the course", course)


student1 = Student("John Doe", "2023001")
student2 = Student("Alice Smith", "2023002")

student1.register_course("Mathematics")
student1.register_course("Physics")
student2.register_course("Biology")

student1.describe_student()
student1.describe_courses()

student2.describe_student()
student2.describe_courses()
