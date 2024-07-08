import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('school.db')

# Create a cursor object
cursor = conn.cursor()

# Fetch and display data from students table
print("Students Table:")
cursor.execute("SELECT * FROM students")
students = cursor.fetchall()
for student in students:
    print(student)

print("\nMarks Table:")
# Fetch and display data from marks table
cursor.execute("SELECT * FROM marks")
marks = cursor.fetchall()
for mark in marks:
    print(mark)

# Close the connection
conn.close()
