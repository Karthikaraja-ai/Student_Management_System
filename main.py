from database import create_database
from operations import (
    add_student,
    view_students,
    search_student,
    update_student,
    delete_student
)

# Create the database and table if they don't exist
create_database()

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        student_id = int(input("Enter Student ID: "))
        search_student(student_id)

    elif choice == "4":
        student_id = int(input("Enter Student ID to Update: "))
        update_student(student_id)

    elif choice == "5":
        student_id = int(input("Enter Student ID to Delete: "))
        delete_student(student_id)

    elif choice == "6":
        print("Thank you for using the Student Management System!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 6.")

