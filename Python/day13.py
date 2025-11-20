# file handling
# read file

f = open("day13_1.text", "r")
print(f.name)
f.close()

with open("day13_1.text", 'r') as f:
    # print(f.read())
    c = f.readlines()
    for line in c:
        print(line, end="")


with open("day13_1.text", 'r') as f:
    print("\n")
    for line in f:
        print(line, end="")

with open("day13_1.text", "r") as f:
    f_content = f.read(20)
    while len(f_content) > 0:
        print(f_content, end="")

        f_content = f.read(20)
# f.tell() -> positon
# f.seek() -> sets start index for f.read

# write file

with open("day13_2.text", "w") as f:
    f.write("second test file")

with open("day13_1.text", "r") as rf:
    with open("day13_2.text", "w") as wf:
        wf.write(rf.read())


with open("day13_1.text", "r") as rf:
    with open("day13_2.text", "w") as wf:
        for line in rf:
            wf.write(line)
