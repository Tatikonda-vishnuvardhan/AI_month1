# string reversal
message = "hello world"
print(message[::-1])

print("*"*30)

# lists
list1 = [20, 20.3, 'hi']
n = len(list1)
print(list1[n-1])
print(list1[-n])
list1[2] = "bye"
print(list1[2])
list2 = [2, 2.5, "hello"]

print("*"*30)

# concatenation
sum01 = list1 + list2
print(sum01)
add = list1[0] + len(list2[2])
print(add)
print(list1*5)
print(20 in list1)
list3 = [1, 2, 3, 4, 5, 6, 7, 8, 1, 1]
m = len(list3)
print(m)
print(list3[0:10:2])
print(list3[5::-1])
print(list3[:-m:-1])
print(list3[::-1])
list4 = list3[2:8]
print(list4[::-1])
print(list3)

print("*"*30)


# day 8
# insert

list3.append("vishnu")
list3.insert(3, "inserted")
x = list3.copy()
y = list3.copy()
z = list3.copy()
x.append(list1)
print(x)
z.insert(1, list1)
print(z)
y.extend(list1)
print(y)

print("*"*30)

# expanding inside lists of lists


def extract(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(extract(item))
        else:
            result.append(item)
    return result


print(extract(z))

print("*"*30)

# remove
list4 = ["math", "physics", "chemistry", "science",
         "english", "telugu", "social", "hindi"]
x = list4.copy()
list4.remove("math")
print(list4)
list4.pop(1)
print(list4)
list4.pop()  # last element
print(list4)
list4.reverse()
print(list4)
list4.sort()  # method overwrites list
print(list4)
y = sorted(x)  # func not changes list
print(y)

print(x)
print(max(x))
print(min(x))
list5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(min(list5))
print(max(list5))
print(sum(list5))
print(list5.index(1))
print(8 in list5)

print("*"*30)

# removing duplicates


def dup(lst):

    dup_list01 = []
    for item in lst:
        if item not in dup_list01:
            dup_list01.append(item)

    return dup_list01


list01 = [1, 2, 3, 4, 5, 1, 3, 1]
print(dup(list01))

list02 = [2, 3, 4, 2, 3, 4, 5, 6]
ans = list(set(list02))
print(ans)

print("*"*30)

# tuples same lists but immutable
tup1 = (1, 2, 3, 2, 1,)
print(tup1)
# swapping
t = (10, 15)
a, b = t
print(f"before swapping a: {a} and b:{b}")
b, a = t
print(f"after swapping a: {a} and b:{b}")

print("*"*30)

# sets
set1 = {1, 2, 3, 4, 1, 3}
set2 = {3, 4, 5, 6, 7}
print(set1)
set1.add(7)
print(set1.__sub__(set2))
print(set1)
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set2.difference(set1))

# set1.intersection_update(set2) edits s1 with intersected items
