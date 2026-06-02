import csv
import os

filename = "students.csv"

# Create file if not exists
if not os.path.exists(filename):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Roll No", "Name", "Marks"])


# Add student
def add_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")

    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([roll, name, marks])

    print("Student added successfully!")


# Show all students
def show_students():
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


# Search student
def search_student():
    roll = input("Enter Roll No to search: ")
    found = False

    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == roll:
                print("Student Found:", row)
                found = True
                break

    if not found:
        print("Student not found!")


# Delete student
def delete_student():
    roll = input("Enter Roll No to delete: ")
    rows = []

    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] != roll:
                rows.append(row)

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print("Student deleted (if existed).")


# Menu
while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Show All Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        show_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice!")