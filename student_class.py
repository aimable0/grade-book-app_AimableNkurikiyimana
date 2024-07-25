class Student:
    """a class that represents/ initiates a student object"""
    courses_registered_list = []

    def __init__(self, email="", names="", courses_registered=[], GPA=""):
        """initializing a student instance"""
        self.email = email
        self.names = names
        self.courses_registered = courses_registered
        self.GPA = GPA

    def calculate_GPA(self):
        # function to be yet completed.
        pass

    def register_for_course(self, course):
        # function to be yet improved.
        self.courses_registered.append[course]
