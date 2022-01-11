#QUESTION 1-AVERAGE OF 3 NO'S
fsrt=int(input("enter first no.:"))
secnd=int(input("enter second no.:"))
thrd=int(input("enter third no.:"))
print("Average of three no.s entered by the user is:",(fsrt+secnd+thrd)/3)
print("\n","*************************","\n")

#QUESTION 2- INCOME TAX
SD= 10000  # standard deduction
DT= 3000    #department deduction
TR= 0.20    # tax rate = 20%
GrossIncome=int(input("enter your gross income:"))
dependents=int(input("enter no of dependendts:"))
TI=GrossIncome-SD-(dependents*DT)  # taxable income
print("Person's income tax is:",TI*TR)
print("\n","*************************","\n")

#QUESTION 3- LIST
student=[21104103, "RISHIT SEHGAL","M","INTRODUCTION TO COMPUTING" , 10.0]
print(student)
print("\n","*************************","\n")

#QUESTION 4-ENTERING MARKS
marks=input("enter marks of 5 student with space in between :").split()
marks.sort()
print(marks)
print("\n","*************************","\n")

#QUESTION 5-COLOR
color=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color.pop(3)
print("after removing 4th element",color)
color[3]="Purple"
print(color)

#END
