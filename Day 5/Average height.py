student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

students = 0
total = 0

for height in student_heights:
    students += 1
    total = total + height

print(round(total / students))