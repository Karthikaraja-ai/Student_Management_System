import sqlite3

# Function to create database and table
def create_database():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        student_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        department TEXT,
        marks REAL,
        grade TEXT
    )
    """)

    conn.commit()
    conn.close()

    print("Database and students table created successfully!")

# Run the function
if __name__ == "__main__":
    create_database()