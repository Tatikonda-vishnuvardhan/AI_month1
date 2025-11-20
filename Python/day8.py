# Student Marks Manager

marks = [85, 92, 78, 64, 90]

print("Original Marks:", marks)

# Average
avg = sum(marks) / len(marks)
print("Average Marks:", avg)

# Highest and Lowest
print("Highest:", max(marks))
print("Lowest:", min(marks))

# Sorted
print("Sorted Marks:", sorted(marks))

# Remove duplicates example
marks_with_dupes = [85, 92, 78, 85, 90, 92]
unique_marks = list(set(marks_with_dupes))
print("Unique Marks:", unique_marks)
