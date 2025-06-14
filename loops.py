Students_marks = input("Enter each StudentsMarks:").split()
Highest = [0]
sorted = []
for mark in range(0, len(Students_marks)):
    Students_marks[mark] = int(Students_marks[mark])

    if Students_marks[mark] > Highest[0]:
        Highest[0] = Students_marks[mark]
    sorted.append(Highest[0])
print("Highest marks are:", sorted)

print("Students marks are:", Students_marks)
print(f"Highest mark  is {Highest[0]}")
