student_name = "Rahul"
marks = [85, 78, 92, 88, 75]
total = 0
for mark in marks:
    total = total + mark
average = total / len(marks)
percentage = (total / 500) * 100
print("Student Name:", student_name)
print("Marks:", marks)
print("Total Marks:", total)
print("Average:", average)
print("Percentage:", percentage)
if percentage >= 90:
    print("Grade: A+")
elif percentage >= 80:
    print("Grade: A")
elif percentage >= 70:
    print("Grade: B")
else:
    print("Grade: C")