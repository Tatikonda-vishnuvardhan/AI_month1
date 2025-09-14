# student managemt adding to student records
class Student:
    def __init__(self, name, age, roll_number):
        self.name = name
        self.age = age
        self.roll_number = roll_number

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Roll No: {self.roll_number}"


def main():

    n = int(input("enter total no of student records: "))
    i = 1
    students = []

    while i in range(1, n+1):
        x = input(f"enter {i} student name:")
        y = int(input(f"enter the age of {i} student:"))
        z = int(input(f"enter the roll number of {i} student:"))
        studenti = Student(x, y, z)
        students.append(studenti)
        i += 1
    i = 1
    print("\nStudent Records: ")
    for student in students:
        print(f"student {i} details -->{student.get_details()}")
        i += 1


if __name__ == "__main__":
    main()
