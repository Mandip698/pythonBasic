# WAP to enter no. of students and enter 5 sub marks, print total marks, percent, and division.
x = int(input("Enter no. of students: "))
i = 1
students_marks = []
while i <= x:
    print(f'====Student : {i}====')
    for mark in range(1):
        nep = int(input("Enter marks of nepali : "))
        eng = int(input("Enter marks of english : "))
        math = int(input("Enter marks of math : "))
        sci = int(input("Enter marks of science : "))
        sco = int(input("Enter marks of pop : "))
        marks = [nep, eng, math, sci, sco]
        students_marks.append(marks)
        i += 1

for students in students_marks:
    total = 0
    for get_mark in students:
        total = +get_mark

    per = total / 5
    div = ''
    if per > 35 and per <= 45:
        div += "Third"
    elif per > 45 and per <= 60:
        div += "Second"
    elif per > 60 and per <= 75:
        div += "First"
    elif per > 75 and per <= 100:
        div += "Distinction"
    else:
        div += "Fail"

    print(f'Total marks: {total} , Percentage: {per}% and Division: {div}')
