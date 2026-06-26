import sqlite3


# -------------------------------
# Grade Calculation
# -------------------------------
def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"


# -------------------------------
# Add Student
# -------------------------------
def add_student():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    student_id = int(input("Enter Student ID: "))
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    department = input("Enter Department: ")
    marks = float(input("Enter Marks: "))

    grade = calculate_grade(marks)

    try:
        cursor.execute("""
        INSERT INTO students
        (student_id, name, age, department, marks, grade)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (student_id, name, age, department, marks, grade))

        conn.commit()
        print("\nStudent added successfully!")

    except sqlite3.IntegrityError:
        print("\nStudent ID already exists!")

    conn.close()


# -------------------------------
# View All Students
# -------------------------------
def view_students():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    if len(students) == 0:
        print("\nNo student records found.")

    else:
        print("\n===== STUDENT RECORDS =====")

        for student in students:
            print("-----------------------------")
            print("Student ID :", student[0])
            print("Name       :", student[1])
            print("Age        :", student[2])
            print("Department :", student[3])
            print("Marks      :", student[4])
            print("Grade      :", student[5])

    conn.close()


# -------------------------------
# Search Student
# -------------------------------
def search_student(student_id):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE student_id=?",
        (student_id,)
    )

    student = cursor.fetchone()

    if student:
        print("\nStudent Found")
        print("-----------------------------")
        print("Student ID :", student[0])
        print("Name       :", student[1])
        print("Age        :", student[2])
        print("Department :", student[3])
        print("Marks      :", student[4])
        print("Grade      :", student[5])
    else:
        print("\nStudent not found!")

    conn.close()


# -------------------------------
# Update Student
# -------------------------------
def update_student(student_id):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE student_id=?",
        (student_id,)
    )

    student = cursor.fetchone()

    if student is None:
        print("\nStudent not found!")
        conn.close()
        return

    print("\nEnter New Details")

    name = input("Name: ")
    age = int(input("Age: "))
    department = input("Department: ")
    marks = float(input("Marks: "))

    grade = calculate_grade(marks)

    cursor.execute("""
    UPDATE students
    SET
        name=?,
        age=?,
        department=?,
        marks=?,
        grade=?
    WHERE student_id=?
    """, (name, age, department, marks, grade, student_id))

    conn.commit()

    print("\nStudent updated successfully!")

    conn.close()


# -------------------------------
# Delete Student
# -------------------------------
def delete_student(student_id):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE student_id=?",
        (student_id,)
    )

    student = cursor.fetchone()

    if student is None:
        print("\nStudent not found!")
    else:
        cursor.execute(
            "DELETE FROM students WHERE student_id=?",
            (student_id,)
        )

        conn.commit()
        print("\nStudent deleted successfully!")

    conn.close()