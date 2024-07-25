import time
from student_class import Student
from grade_book_class import GradeBook
from course_class import Course

#welcome message
print('------------------------------------------')
print('\nWelcome to the Grade Book Application!\n')

active = True

while active:
    print('\n-----------------MAIN MENU----------------\n')
    
    # printing possible choices
    print("Please select an action:\n")
    print("1. Add Student")
    print("2. Add Course")
    print("3. Register Student for course")
    print("4. Calculate Ranking")
    print("5. Search by Grade")
    print("6. Generate Transcript")
    print("7. Exit\n")
    
    # retrieving user's choice
    choice = (input('Enter your choice: '))
    print()  # empty line for readability

    print('-----------------MENU END----------------\n')
    try:
        choice = int(choice)
    except ValueError:
        print('Choice can only be a number.')
        active = return_to_main()
    
    def return_to_main():
        answer = input('Return to main menu [y/n]: ')
        if answer == 'y':
            return True
        elif answer == 'n':
            print("Good bye!\n")
            return False

    #working with user's choice
    if choice in range (1, 7):
        if choice == 1:
            grade_book = GradeBook()
            grade_book.add_student()
            active = return_to_main()

        if choice == 2:
            grade_book = GradeBook()
            grade_book.add_course()
            active = return_to_main()

        if choice == 3:
            grade_book = GradeBook()
            grade_book.register_student_for_course()
            active = return_to_main()
    
        if choice == 4:
            pass

        if choice == 5:
            pass

        if choice == 6:
            pass

    elif choice  == 7:
        print("Closing ...")
        time.sleep(1)
        print('Almost done ...')
        time.sleep(0.5)
        print("Good bye!\n")
        active = False
    else:
        print("Invalid choice!\n")
        active = return_to_main()
