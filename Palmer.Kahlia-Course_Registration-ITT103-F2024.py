# Classes for the Course, Student and RegistrationSystem

class Course:
    def __init__(self):
        self.course_id = ""
        self.course_name = ""
        self.fee = ""


class Student:
    def __init__(self):
        self.student_id = ""
        self.student_name = ""
        self.email = ""
        self.balance = 0.0
        self.courses = []


class RegistrationSystem:
    def __init__(self):
        self.courses = []
        self.registered_students = {}
        self.total_payed = 0

#Method to check the courses registered to the student
    def check_student_courses(self, student_id, course_name):
        if student_id in self.registered_students:
            data = self.registered_students[student_id]
            for courses in data.courses:
                if courses == course_name:
                    print("Course found")
                    return True
                else:
                    print("Course not found")
                    return False


        else:
            print("Student not found")
            return False

#Method for retrieving the course name for the course ID entered
    def get_course_name(self, course_id):
        for course in self.courses:
            if course.course_id == course_id.lower():
                return course.course_name
        return False

#Method that checks if the course ID exists
    def search_course(self, course_id):
        for course in self.courses:
            if course.course_id == course_id.lower():
                return True
        return False

#Method for checking if the student ID entered exists
    def search_student_id(self, id_num):
        if id_num in self.registered_students:
            return True
        else:
            return False

    # Method to add courses to the list of offered courses
    def add_course(self, course_id, course_name, fee):
        new_course = Course()
        if self.search_course(course_id) is True:
            print("Course already exists in available courses")
            return
        else:
            new_course.course_id = course_id.lower()
            new_course.course_name = course_name
            new_course.fee = fee
            self.courses.append(new_course)
            print("Course now available to enroll students")

    # Method to register students
    def register_student(self, student_id, student_name, email):
        if self.search_student_id(student_id) is True:
            print("Duplicate entry! student ID already exist")
        else:
            new_student = Student()
            new_student.student_id = student_id
            new_student.student_name = student_name
            new_student.email = email
            self.registered_students[new_student.student_id] = new_student
            print("\nStudent has been registered")

    # Enroll Students in Courses
    def enroll_in_course(self, student_id, course_id):
        student_data = self.registered_students[student_id]
        avail_courses = self.get_course_name(course_id)
        if avail_courses is False:
            print("No course found with the course ID entered")
            return

        if self.check_student_courses(student_id, avail_courses) is True:
            print("Student already registered for this course")
            return

        else:
            for course in self.courses:
                if course.course_id == course_id:
                    student_data.courses.append(course.course_name)
                    student_data.balance += course.fee
                    print("\nCourse successfully added to student list")

#Method to calculate payments towards a course and for the required 40% payment to be made to fully register students
    def calculate_payment(self, student_id, user_payment):

        student_data = self.registered_students[student_id]
        req_to_register = student_data.balance * 0.4
        self.total_payed += user_payment
        student_data.balance -= user_payment

        if user_payment >= req_to_register:
            student_data.balance - user_payment
            print("You have successfully made your payment. Your balance is"
                  "$", student_data.balance, ".")
            return


        if user_payment < req_to_register:
            if self.total_payed < req_to_register:
                student_data.balance - user_payment
                print(f"Minimum balance required to reqister not met. please make a payment of"
                      f"${req_to_register-self.total_payed} in order to be qualified for registration")
            else:
                student_data.balance - user_payment
                print("You have successfully made your payment. Your balance is"
                      "$", student_data.balance, ". You have now met the minimum requirement to be registered")
                return

#Method to show the remaining balance of a student for the courses they are registered to
    def check_student_balance(self, student_id):
        if self.search_student_id(student_id) is False:
            print("No student found with the ID entred")
            return
        else:
            student_data = self.registered_students[student_id]
            print("Your account balance is $", student_data.balance)

#Method for showing available courses
    def show_courses(self):
        print("*************Available courses***************\n")
        for courses in self.courses:
            print("Course name:", courses.course_name, "|Course code: (", courses.course_id, ")")

#Method for showing registered students
    def show_registered_students(self):
        data = self.registered_students
        print("************Registered Students**************\n")
        for students in data:
            print("Student ID:", students, "|Student Name: ", data[students].student_name, "|Email: ",
                  data[students].email)

#Method for showing students registered in a course
    def show_students_in_course(self, c_id):
        c_name = self.get_course_name(c_id)
        print("\n*********Students enrolled in", c_name, "***********" "\n")
        for key, value in self.registered_students.items():
            if c_name in self.registered_students[key].courses:
                print("Student Name: ", self.registered_students[key].student_name)


system = RegistrationSystem()

while True:
    print("\nMain menu\n")

    choice = input("1. Register Student\n2. Add Course\n3. Enroll in Course\n"
                    "4. Calculate Payment\n5. Check Student Balance\n6. Show Courses\n7. Show Registered Students\n"
                    "8. Show Students in a Course\n9. Exit\nSelect an option: ").lower()

# Conditional statements within While loop
    if choice == "1":
        try:
            stud_id = int(input("Enter yor student ID: "))
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            system.register_student(stud_id, name, email)
        except ValueError:
            print("Please enter a correct response!")



    elif choice == "2":
        try:
            course_id = input("Enter course ID: ").lower()
            course_name = input("Enter course name: ")
            fee = float(input("Enter course cost: "))
            system.add_course(course_id, course_name, fee)
        except ValueError:
            print("Enter a correct value!")

    elif choice == "3":
        try:
            student_id = int(input("Enter student ID: "))
            if system.search_student_id(student_id) is False:
                print("Student with ID", student_id, "Not found")

            else:
                course_id = input("Enter course ID: ").lower()
                system.enroll_in_course(student_id, course_id)
        except ValueError:
            print("Enter a correct value!")

    elif choice == "4":
        try:
            sub_menu = True
            print("Disclaimer\nA payment of 40% of the total balance is needed to be registered\n")
            while sub_menu:
                user_option = input("1. Make a payment\n2. Exit to previous menu\n"
                                    "Choose an option: ")

                if user_option == "1":
                    student_id = int(input("Enter your student ID: "))
                    if system.search_student_id(student_id) is False:
                        print("Student with ID", student_id, "Not found")
                        break
                    else:
                        payment = float(input("Enter the amount you want to pay: "))
                        system.calculate_payment(student_id, payment)

                else:
                    sub_menu = False
        except ValueError:
            print("Enter a correct value!")

    elif choice == "5":
        try:
            student_id = int(input("Enter your student ID: "))
            system.check_student_balance(student_id)
        except ValueError:
            print("Enter a correct value!")

    elif choice == "6":
        system.show_courses()

    elif choice == "7":
        system.show_registered_students()

    elif choice == "8":
        course_id = input("Enter course ID: ").lower()
        system.show_students_in_course(course_id)

    elif choice == "9":
        break

    else:
        print("Please enter a valid selection!")




