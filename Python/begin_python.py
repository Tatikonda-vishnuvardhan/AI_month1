first = "vishnu"
last = "vardhan"
total = f"{len(first)}  {len(last)}"
print(total)
total = f"{first}  {last}"
print(total)
course = "python programming"
print(course.upper())
print(course.lower())
print(course.title())
print(course.strip())
print(course.find("pro"))
print(course.replace("p", "j"))
print(10 * 3)
print(10 + 3)
print(10 / 3)
print(5 // 2)
print(10 ** 3)
print(10 % 3)
print(type(course))
x = int(input("get number :"))
y = x + 5
print(f"x: {x}, y: {y}")  # format string

print("*"*30)

# if and if else stements
age = int(input("enter age:"))
if age >= 21:
    print("eligible to vote")
else:
    print("not eligible")
if 18 <= age < 65:
    print("eligible to vote")
else:
    print("not eligible")

print("*"*30)

# tronsfrom of if statements
message = "eligible" if age >= 21 else "not eligible"
print(message)

print("*"*30)

# and or not statement
high_credit = True
high_income = False
student = False

if high_credit and high_income:
    print("eligible for credit card")
else:
    print("not eligible")
if high_credit or high_income:
    print("eligible for credit card")
else:
    print("not eligible")
if (high_credit or high_income) and not student:
    print("eligible for credit card")
else:
    print("not eligible")

print("*"*30)

# for statements and for else
for num in range(1, 10):
    print(num*".", num)
succes = False
for n in range(3):
    print("attempt", n)
    if succes:
        print("success")
        break
else:
    print("failure")
for x in range(3):
    for y in range(3):
        print(f"({x} ,{y})")

print("*"*30)

# whileloop
value = 100
while value > 0:
    print(value)
    value //= 2
n = len(range(1, 10))
for num in range(1, 10):
    if num % 2 == 0:
        print(num)
print(f"we have {(n-1)//2} even numbers")
count = 0
for num in range(1, 10):
    if num % 2 == 0:
        print(num)
        count += 1
print(f"we have {count} even numbers")

print("*"*30)

# 1.function performs task


def greet(first_name, last_name):
    print(f"hi {first_name} {last_name}")
    print("welcome")


greet(23, "tatikonda")

print("*"*30)

# 2.funtion return value


def greet_new(first_name, last_name):
    return f"hi {first_name} {last_name}"


message = greet_new("v", "t")
print(message)
