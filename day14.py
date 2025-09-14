# Final Student Management combining all days

import json


class Student:
    def __init__(self, name, age, roll_number, subject=None):
        self.name = name
        self.age = age
        self.roll_number = roll_number
        self.subject = subject if subject else []

    def get_details(self):
        return {
            "name": self.name,
            "age": self.age,
            "roll_number": self.roll_number,
            "subject": self.subject

        }


def save_students(students, file_name="day14_students.json"):
    try:
        with open(file_name, "w") as wf:
            data = [s.get_details() for s in students if s]
            json.dump(data, wf, indent=4)
            print("Successfully saved")
    except:
        print("Error while saving file")
        return []


def load_students(file_name="day14_students.json"):
    try:
        with open(file_name, "r") as rf:
            data = json.load(rf)

            return [Student(**s) for s in data]
    except:

        return []


def find_student(students, roll):
    for s in students:
        if s.roll_number.lower() == roll.lower():
            print("successfuly found")
            return s

    return None


def main():
    students = load_students()
    while True:
        print("Available operations\n")
        print("Enter 1 for adding students.\n")
        print("Enter 2 for veiwing students in file.\n")
        print("Enter 3 for updating students or any details of sudents.\n")
        print("Enter 4 for searching students\n")
        print("Enter 5 for delete students.\n")
        print("Enter 6 for saving and exit.\n")
        try:

            choice = int(input("Enter your choice:").strip())

        except:
            print("Enter integer:")
            continue

        if choice == 1:
            name = input("Enter name of the student:")
            while True:
                try:
                    age = int(input("Enter age:"))
                    break
                except:
                    print("Enter age in numbers")
                    continue

            subjects = input(
                "Enter the subjects(comma seperated):").split(",")
            subjects = [s.strip() for s in subjects if s.strip()]
            while True:
                roll_number = input("Enter unique roll number")
                if any(s.roll_number.lower() == roll_number.lower() for s in students):
                    print("Roll number already exists!")
                    continue
                else:

                    student = Student(name, age, roll_number, subjects)
                    students.append(student)
                    save_students(students)
                    print("Student added!")
                    break

        elif choice == 2:
            if students:

                for s in students:
                    print(
                        f"Name: {s.name}, Age: {s.age}, Roll: {s.roll_number}, Subjects: {', '.join(s.subject)}")

            else:
                print("No records")
        elif choice == 3:
            roll = input("Enter roll_number for updating")
            student = find_student(students, roll)

            if student:

                print("Enter new details ")
                new_name = input(
                    f"Enter name of the student({student.name}):") or student.name
                new_age = input(f"Enter age({student.age}):")
                try:
                    student.age = int(new_age) if new_age else student.age
                except:
                    print("Invalid age type entered keeping old age record")
                while True:

                    new_roll_number = input(
                        f"Enter  unique roll number({student.roll_number})")
                    if any(s.roll_number.lower() == new_roll_number.lower() and s != student for s in students):
                        print("Roll number already exists!")
                        continue
                    else:
                        new_roll_number = new_roll_number if new_roll_number else student.roll_number
                        break
                new_subjects = input(
                    f"Enter the subjects(comma seperated)({student.subject}):")
                new_subjects = [s.strip()
                                for s in new_subjects.split(",") if s.strip()]
                student.name = new_name

                student.roll_number = new_roll_number
                student.subject = new_subjects if new_subjects else student.subject
                save_students(students)
                print("Updated successfully!")
            else:
                print("Not found")

        elif choice == 4:

            sub_choice = input(
                "Enter 'a' for searching using roll number and 'b' for searching using name:").lower()
            if sub_choice == 'a':
                roll = input("Enter roll number:")
                found = find_student(students, roll)
                if found:
                    print(
                        f"Name: {found.name}, Age: {found.age}, Roll: {found.roll_number}, Subjects: {', '.join(found.subject)}")

                else:
                    print("Not found")
            elif sub_choice == 'b':
                search_name = input(
                    "Enter name(partial name) for searching:").lower()
                search_list = []
                for student in students:
                    if search_name in student.name.lower():
                        search_list.append(student)
                if search_list:
                    for s in search_list:
                        print(
                            f"Name: {s.name}, Age: {s.age}, Roll: {s.roll_number}, Subjects: {', '.join(s.subject)}")

                else:
                    print("Not found")
            else:
                print("Invalid serach type")

        elif choice == 5:
            roll = input("Enter roll number to delete: ")
            student = find_student(students, roll)

            if student:
                confirm = input(
                    f"Are you sure you want to delete {student.name} records? ((y,yes)/(n,no): ").lower()
                if confirm in {"y", "yes"}:
                    students.remove(student)
                    save_students(students)
                    print(" Student deleted successfully!")
                else:
                    print(" Deletion cancelled.")
            else:
                print(" Student not found!")
        elif choice == 6:
            if students:
                save_students(students)
            else:
                print("No record to save")

            confirm = input("Do you want exit (yes,y)/(no,n)").lower()
            if confirm in {"y", "yes"}:
                print("Existed successfully")
                break
            else:
                continue
        else:
            print("Entered invalid choice choose  between 1-6.")


if __name__ == "__main__":
    main()
