student_grades = {}
# Add a new student
def add_student(name , grade):
    student_grades[name] = grade
    print(f"added {name} with a {grade}")

def update_student(name , grade):
    if name in student_grades:
        student_grades[name]= grade    
        print(f"{name} with marks are updated {grade}")
    else:
        print(f"{name} is not found!")

def delete_student(name):
    if name in student_grades:
        del student_grades[name]

        print(f"{name} has been successfully delete")
    else:
        print(f"{name} is not found!")

def display_all_students():
    if student_grades:
        for name , grade in student_grades.items():
            print(f"{name} : {grade}")
    else:
        print("no students found/added")

def main():
    while True:
        print("\n---Student grades management system---")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View Students")
        print("5. Exit")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue
        if choice == 1:
            name = input("Enter student name: ")
            try:
                grade = int(input("Enter student grade: "))
            except ValueError:
                print("Invalid grade! Please enter a number.")
                continue
            add_student(name, grade)
        elif choice == 2:
            name = input("Enter student name: ")
            try:
                grade = int(input("Enter student grade: "))
            except ValueError:
                print("Invalid grade! Please enter a number.")
                continue
            update_student(name, grade)
        elif choice == 3:
            name = input("Enter student name: ")
            delete_student(name)
        elif choice == 4:
            display_all_students()
        elif choice == 5:
            print("Closing the program")
            break
        else:
            print("Invalid choice")
main()

          


                  














    
