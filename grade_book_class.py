from student_class import Student
from course_class import Course
import json
import os

class GradeBook(Student):
    """doc string"""
    #defening class attributes and functions
    # Initializing the lists
    student_list = []
    course_list = []
    
    # STUDENT LIST FUNCTIONS
    # Function to write the list to a file
    def write_list_to_file(filename, list_to_write):
        with open(filename, 'w') as file:
            json.dump(list_to_write, file)

    # Function to append names to the list and update the file
    def append_name_and_update_file(name, filename):
        GradeBook.student_list.append(name)
        GradeBook.write_list_to_file(filename, GradeBook.student_list)

    # Initialize the file with an empty list
    filename = 'student_list.json'

    # COURSE LIST FUNCITONS
    def create_course_list_file(courses_filename, course_list):
        with open(courses_filename, 'w') as f:
            json.dump(course_list, f)
    
    def update_and_append_c_file(course_name, courses_filename):
        GradeBook.course_list.append(course_name)
        GradeBook.create_course_list_file(courses_filename, GradeBook.course_list)

    #initializing gradebook class
    def __init__(self, email="", names="", courses_registered="", GPA="", student_list=[], course_list=[]):
        super().__init__(email, names,  courses_registered, GPA)
        """doc string"""
    
    course_filename = "course_list.json"

    def add_student(self):
        # creating student instance.
        student_email = input('Enter student email: ')
        student_name = input('Enter student names: ')
        student = Student(student_email, student_name)
        
        #adding name to the file
        GradeBook.append_name_and_update_file(student_name, GradeBook.filename)
        print("\nRecorded Successfully!\n")

    def add_course(self):
        #creating a course instance
        course_name = input('Enter course name: ')
        course_trimester = input('Enter course trimester: ')
        course_credits = input('Enter course credits: ')
        course = Course(course_name, course_trimester, course_credits)
        
        #adding course to list file
        GradeBook.update_and_append_c_file(course_name, GradeBook.course_filename)
        print("\nCourse added succesfully!\n")


    def register_student_for_course(self):
        name = input('Enter student name: ')
        with open('student_list.json', 'r', encoding='utf-8') as f:
            names = f.read()
        if name not in names:
            print(">Student can't be found.\n")
            return 1

        course = input('Enter course name: ')
        with open('course_list.json', 'r', encoding='utf-8') as file:
            courses = file.read()
        if course not in courses:
            print('Course not available.')
            print('Registration failed, try again!')
            
        else:
            Student.register_for_course(course)
            print('Registration complete.\n')


    def calculate_GPA(self):
        pass

    def calculate_ranking(self):
        pass

    def search_by_grade(self):
        pass

    def generate_transcript(self):
        pass
    
    #verification
    def print_list(self):
        return "aimable"