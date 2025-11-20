# inheritence
# Base Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}"


# Child Class - Student inherits Person
class Student(Person):
    def __init__(self, name, age, roll_number):
        super().__init__(name, age)  # call parent constructor
        self.roll_number = roll_number

    def get_details(self):
        return f"{super().get_details()}, Roll No: {self.roll_number}"


# Child Class - Teacher inherits Person
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def get_details(self):
        return f"{super().get_details()}, Subject: {self.subject}"


# Demo
s1 = Student("Alice", 20, "S101")
t1 = Teacher("Mr. Bob", 40, "Mathematics")

print(s1.get_details())
print(t1.get_details())


# extension

# Base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}"


# Student class
class Student(Person):
    def __init__(self, name, age, roll_number):
        super().__init__(name, age)
        self.roll_number = roll_number
        self.subjects = []  # list of subjects

    def enroll_subject(self, subject):
        self.subjects.append(subject)

    def get_details(self):
        subj_names = []
        if self.subjects:

            for subj in self.subjects:
                subj_names.append(subj.title)
        else:
            subj_names = None

        return f"{super().get_details()}, Roll No: {self.roll_number}, Subjects: {subj_names}"


# Teacher class
class Teacher(Person):
    def __init__(self, name, age, subject=None):
        super().__init__(name, age)
        self.subject = subject

    def assign_subject(self, subject):
        self.subject = subject

    def get_details(self):
        if self.subject:
            subject_name = self.subject.title
        else:
            subject_name = "None"
        return f"{super().get_details()}, Teaches: {subject_name}"


# Subject class
class Subject:
    def __init__(self, title, code):
        self.title = title
        self.code = code

    def get_details(self):
        return f"Subject: {self.title}, Code: {self.code}"


# --------- Polymorphism in action ---------
# Create subjects
math = Subject("Mathematics", "MATH101")
physics = Subject("Physics", "PHY101")

# Create student and teacher
alice = Student("Alice", 20, "S101")
bob = Teacher("Mr. Bob", 40)

# Assign subject to teacher
bob.assign_subject(math)
bob.assign_subject(physics)

# Enroll student in subjects
alice.enroll_subject(math)
alice.enroll_subject(physics)  # overwrites as only one subject assigned

# Polymorphic behavior
people = [alice, bob, math, physics]

for i in people:
    print(i.get_details())
