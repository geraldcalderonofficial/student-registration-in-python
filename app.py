student_list = []

def create_student():
    name = input("Please enter the new student name: ")
    student_data = {
        'name': name,
        'marks': []
    }

    return student_data

def add_mark(student, mark):
    student['marks'].append(mark)

def calculate_average_mark(student):
    number = len(student['marks'])

    total = sum(student['marks'])
    return total / number

def print_student_details(student):
    print("{}, average mark: {}.".format(student['name'],
                                         calculate_average_mark(student)))

def print_student_list(students):
    for i, student in enumerate(students):

def menu():
    selection = input("Enter 'p' to print the student list, "
                      "'s' to add a new student, "
                      "'a' to add a mark to a student, "
                      "or 'q' to quit. "
                      "Enter you selection: ")
    while selection != 'q':
        if selection == 'p':
            print_student_list(student_list)
        elif selection == 's':
            student_list.append(create_student())
        elif selection == 'a':

        selection = input("Enter 'p' to print the student list, "
                          "'s' to add a new student, "
                          "'a' to add a mark to a student, "
                          "or 'q' to quit. "
                          "Enter you selection: ")

menu()

#missing code - can be provided upon request.