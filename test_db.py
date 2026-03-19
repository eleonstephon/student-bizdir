import sqlite3
from flask import Flask

app = Flask(__name__)

# STEP 1: Create and fill a test database 

def setup_test_database():
    """
    Creates a test database with a students table
    and inserts 3 fake students into it.
    This runs once when the app starts.
    """
    conn = sqlite3.connect("test.db")
    conn.row_factory = sqlite3.Row

    # Create the students table
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS students (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            name    TEXT NOT NULL,
            course  TEXT NOT NULL
        );
    """)

    # Insert 3 fake students (only if table is empty)
    existing = conn.execute("SELECT COUNT(*) FROM students").fetchone()[0]
    if existing == 0:
        conn.execute("INSERT INTO students (name, course) VALUES (?, ?)", ("Pipi", "Cybersecurity"))
        conn.execute("INSERT INTO students (name, course) VALUES (?, ?)", ("Amara", "Computer Science"))
        conn.execute("INSERT INTO students (name, course) VALUES (?, ?)", ("Kwame", "Civil Engineering"))
        conn.commit()
        print("✅ Test database ready with 3 students!")
    
    conn.close()

# Run setup when app starts
setup_test_database()

#  STEP 2: Flask route that fetches from database 

@app.route("/")
def show_students():
    """
    Fetches all students from the database
    and displays them in the browser.
    """
    conn = sqlite3.connect("test.db")
    conn.row_factory = sqlite3.Row

    students = conn.execute("SELECT * FROM students").fetchall()
    conn.close()

    # Build a simple HTML page showing all students
    html = "<h1>Students List</h1><ul>"
    for student in students:
        html += f"<li>{student['name']} — {student['course']}</li>"
    html += "</ul>"

    return html

if __name__ == "__main__":
    app.run(debug=True)