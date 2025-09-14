class Student:
    def __init__(self, name, age, roll_number):
        self.name = name
        self.age = age
        self.roll_number = roll_number
        self.subjects = []  # new attribute

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Roll No: {self.roll_number}, Subjects: {', '.join(self.subjects) if self.subjects else 'None'}"

    def update_age(self, new_age):
        self.age = new_age
        print(f"{self.name}'s age updated to {self.age}")

    def add_subject(self, subject):
        if subject not in self.subjects:
            self.subjects.append(subject)
            print(f"{subject} added to {self.name}'s subjects")
        else:
            print(f"{self.name} already enrolled in {subject}")

    def get_subjects(self):
        return f"Subjects are:{self.subjects}"


# ---------- MAIN ----------
def main():
    # Create students
    s1 = Student("Alice", 20, 101)
    s2 = Student("Bob", 21, 102)

    # Add subjects
    s1.add_subject("Math")
    s1.add_subject("Physics")
    s2.add_subject("Computer Science")

    # Update age
    s1.update_age(21)

    # Print details
    print("\n--- Student Details ---")
    print(s1.get_details())
    print(s2.get_subjects())


if __name__ == "__main__":
    main()
