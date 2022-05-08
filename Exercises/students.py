# WAP to enter no. of students and enter 5 sub marks, print total marks, percent, and division.
x = int(input("Enter no. of students: "))
i = 0
while i <= x:
    print(f'====Student : (i)====')
    for mark in range(1):
        nep = int(input("Enter marks of nepali : "))
        eng = int(input("Enter marks of english : "))
        math = int(input("Enter marks of math : "))
        sci = int(input("Enter marks of science : "))
        sco = int(input("Enter marks of pop : "))
        total = nep + eng + math + sci + sco
        per = total / 5
        print(f'The total and percentage of students are {total} and {per}%')
        i += 1

