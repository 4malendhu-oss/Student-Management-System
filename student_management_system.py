students = {}

while True:
    print("\n========== Student Management System ==========")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Search Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        students[name] = marks
        print("Student added successfully!")

    elif choice == "2":
        if students:
            print("\nStudent Records:")
            for name, marks in students.items():
                print(f"{name} : {marks}")
        else:
            print("No student records found.")

    elif choice == "3":
        name = input("Enter student name: ")
        if name in students:
            marks = int(input("Enter new marks: "))
            students[name] = marks
            print("Student record updated.")
        else:
            print("Student not found.")

    elif choice == "4":
        name = input("Enter student name to delete: ")
        if name in students:
            del students[name]
            print("Student deleted.")
        else:
            print("Student not found.")

    elif choice == "5":
        name = input("Enter student name to search: ")
        if name in students:
            print(f"{name} : {students[name]}")
        else:
            print("Student not found.")

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice.")