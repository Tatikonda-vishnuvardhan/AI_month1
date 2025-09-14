class Residents:
    apartment_name = "Gayatri toweers"  # class variable
    no_of_residents = 0

    def __init__(self, name, age, flat_no,):
        # instance variable
        self.name = name
        self.age = age
        self.flat_no = flat_no
        Residents.no_of_residents += 1

        self.first_name = name.split()[0]
        self.last_name = name.split()[-1]

    def split_name(self):
        return f"first name:{self.first_name},last name:{self.last_name}"

    def get_details(self):
        return f"name:{self.name},age:{self.age},flat_no:{self.flat_no}"


# object creation
resident1 = Residents("vishnu tatikonda", 21, 2209)
resident2 = Residents("ramesh sheh", 41, 1109)
resident3 = Residents("varun vangaveeti", 25, 3309)
print(resident1.get_details())
print(resident1.age)
print(resident1.split_name())
print(resident2.get_details())
print(resident2.split_name())
print(resident3.get_details())
print(resident3.split_name())
print(
    f"Apartment name is {Residents.apartment_name} and total resdents is {Residents.no_of_residents}")

print("*"*30)

# inheritance(simple)


class Person:
    a = 2.5

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        return f" Name : {self.name}. \n Age : {self.age}."


class student(Person):
    a = 5
    pass


s1 = Person("Vishnu tatikonda", 21)  # parent object
s2 = student("Nihan", 5)  # child object
print(s1.get_details())
print(s2.get_details())
print(s1.a)  # overriding
print(s2.a)

print("*"*30)

# inheritance(complex)


class employee:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        return f"Name : {self.name}. \n Age : {self.age}."


class dev(employee):
    def __init__(self, name, age, pos):
        super().__init__(name, age)
        self.pos = pos

    def get_details(self):

        return f" {super().get_details()} \n Position : {self.pos}"


class manager(employee):
    def __init__(self, name, age, employes=None):
        super().__init__(name, age)
        if employes is not None:
            self.employes = employes
        else:
            self.employes = []

    def add_employee(self, emp):
        if emp not in self.employes:
            self.employes.append(emp)
            print(f"succesfully added")
        else:
            print("already in list")

    def remove_employe(self, emp):
        if emp in self.employes:
            self.employes.remove(emp)
            print(f"succesfully removed ")
        else:
            print("not found")

    def get_details(self):
        emp_list = [emp.name for emp in self.employes]
        return f"{super().get_details()} \n employee list : {emp_list}"

    def employe_list_details(self):
        for emp in self.employes:
            print(emp.get_details())


d1 = dev("Vishnu tatikonda", 21, "junior AI intern")  # child object
d2 = dev("naresh  tnm", 33, "python dev")  # child object
e2 = employee("Nihan", 5)  # parent object
m1 = manager("Naren", 42, [d1])
print(d1.get_details())
print(d2.get_details())
print(e2.get_details())
m1.add_employee(d2)

print(m1.get_details())
m1.remove_employe(d1)

m1.employe_list_details()

print("*"*30)


# multiple, multiple inheritance

class animal:
    def __init__(self, name):
        self.name = name

    def sleep(self):
        print(f"{self.name} is asleep")

    def eat(self):
        print(f"{self.name} is eating")


class prey(animal):
    def flee(self):
        print(f"{self.name} is fleeing")


class predator(animal):
    def hunt(self):
        print(f"{self.name} is hunting")


class herbivorious(prey):  # multilevel
    pass


class carnivariuos(prey, predator):  # multiple
    pass


h1 = herbivorious("deer")
c1 = carnivariuos("fox")

h1.sleep()
h1.eat()
h1.flee()
# h1.hunt()
c1.sleep()
c1.eat()
c1.flee()
c1.hunt()

print("*"*30)
