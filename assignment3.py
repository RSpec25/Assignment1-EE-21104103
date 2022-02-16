# QUESTION-1 NO. OF OCCURENSE OF WORDS/LETTERS
print("---------------------")
print("     SOLUTION 1     ")
print("---------------------")
str1=input("Enter a string:")
str=[]                                      #empty list to store different words
str=str1.lower().split()
if(len(str)>1):                             #code for more than 1 word input
    for i in range(len(str)):               #printing occurrence of each word
        print(f"no. of occurrences of %s is:%d"%(str[i],str.count(str[i])))
elif(len(str)==1):                          #code for single word input
    str2=str[0]                             #creating a list of letters
    print(str2)
    for i in range(len(str2)):              #printing occurrence of each letter
        print(f"no. of occurrence of %s is:%d"%(str2[i],str2.count(str2[i])))
else:
    print("no valid string entered")


print("---------------------")
#  QUESTION 2 PRINTING NEXT DATE OF THE DATE ENTERED BY THE USER
print("     SOLUTION 2     ")
print("---------------------")
print("Enter the date\n1.month(1-12)\n2.day(1-31)\n3.year(1800-2025)")
month=int(input())
day=int(input())
year=int(input())
if(1<=month<=12 and 1<=day<=31 and 1800<=year<=2025):                     #checking the condition given in the question
    if ((year% 400 == 0) or (year % 100 != 0) and (year % 4 == 0)):       #cheaking wether it is leap year
        print("Leap year")
        if (month in (4, 6, 9, 11) and day == 31) or (month == 2 and day > 29):
            print("invalid date")                                         #checking invalid dates as some moths only contain 30 days
        else:
            if month == 2:                    # n_days= no. of days in the given month
                n_days = 29
            elif month in (4, 6, 9, 11):
                n_days = 30
            else:
                n_days = 31
            if day == n_days:                # if it is month ending
                day = 1
                month+=1
            else:
                day += 1
            if month == 12:                 # if it is end of the year
                month = 1
                year += 1

            date = f"{day}/{month}/{year}"
            print("The Next Date is : ", date)
    else:
        print("not a leap year")          # not a leap year
        if (month in (4, 6, 9, 11) and day == 31) or (month == 2 and day > 28):    #checking invalid dates as some moths only contain 30 days
            print("invalid date entered")
        else:
            if month == 2:               # n_days= no. of days in the given month
               n_days = 28
            elif month in (4, 6, 9, 11):
                n_days = 30
            else:
                n_days = 31
            if day == n_days:           # if it is month ending
                day = 1
                month+=1
            else:
                day += 1
            if month == 12:              # if it is end of the year
                month = 1
                year += 1
            date = f"{day}/{month}/{year}"
            print("The Next Date is : ", date)
else:
    print("wrong input!!!")             # entered date is out of the condition given by user
print("---------------------")
# QUESTION 3- LIST OF TUPLES
print("     SOLUTION 3     ")
print("---------------------")
list1=[]                                # creating empty list
list2=[]
n=int(input(print("enter the no. of elements to be entered in list\n")))
for i in range(0,n):                    # taking input in list
    print("enter the integer value:", i + 1)
    list1.append(int(input()))
for i in range(0,n):                    # making second list with square of elements of first list
    list2.append(list1[i]*list1[i])
list3=list(zip(list1,list2))            # making tuple with first elements from list1 and second element from list 2
print(list3)

print("---------------------")
# QUESTION 4-GRADING SYSTEM
print("     SOLUTION 4     ")
print("---------------------")
grade_point=int(input(print("enter grade within range 4-10(extreme values included):")))
if 4<=grade_point<=10:                                              # making switch case for each grade point
    switcher = {
        10:"Your Grade is 'A+' and Outstanding Performance",
        9 :"Your Grade is 'A' and Excellent Performance",
        8 :"Your Grade is 'B+' and VeryGood Performance",
        7 :"Your Grade is 'B' and Good Performance",
        6 :"Your Grade is 'C+' and Average Performance",
        5 :"Your Grade is 'C' and BelowAverage Performance",
        4 :"Your Grade is 'D' and Poor Performance",
    }
    print(switcher.get(grade_point))                                # printing grade according to grade point
else:
    print("Error!!! invalid grade entered")
print("---------------------")
# QUESTION 5-PATTERN
print("     SOLUTION 5     ")
print("---------------------")
lines = 6                                # lines=no. of lines in pattern
for i in range(lines):

    for j in range(i):                   # loop for printing space
        print(" ", end='')

    for m in range(2 * (lines - i) - 1): # loop for printing alphabets
        print(chr(65 + m), end='')       # using ASCII value
    print()
print("---------------------")
# QUESTION6= STUDENT SID DICTIONARY
print("     SOLUTION 6     ")
print("---------------------")
student_dict={}                                     # creating empty dictionary
while(1):
    user_input=input(print("Y/N or y/n"))           # taking input yes or no with y/n
    if user_input=='Y' or user_input=='y':          # taking names and sid of students
        print("enter SID of student:")
        SID=input()
        print("enter name of the student:")
        name=input()
        student_dict.update({SID:name})             # entering in dictionary
    elif user_input=='N' or user_input=='n':        # getting out of loop no entered by users
        break
    else:
        print("Wrong Input, please enter correct input.")
print("(A) student details entered:\n",student_dict)                # printing dictionary entered by user
print("(B) sorted dictionary using student name:")
sorted_names=sorted(student_dict.items(), key= lambda x:x[1])       # sorted_name= dict sorted by names
print(sorted_names)
print("(C) sorted dictionary using SIDs:")
sorted_SID=sorted(student_dict)                                     # sorted_SID= list of sorted sids
SID_dict={}                                                         # creating of empty dict
for SID in sorted_SID:                                              # entering values in dict(SID_dict) that is sorted by sid
    SID_dict[SID]=student_dict[SID]
print(SID_dict)
print("(D) enter SID")                                                   # printing name of student from sid
S1=input()
print(f"the name of the student with %s is %s"%(S1,student_dict[S1]))

print("---------------------")
# QUESTION 7- FIBONACCI SEIES AND AVERAGE
print("     SOLUTION 7     ")
print("---------------------")
n_term=int(input(print("enter the nth terms of fibonacci series")))
sum=0
# function to calculate fibonacci
def Fibonacci(n_term):
    if n_term < 0:
        print("Incorrect input")

    elif n_term == 0:
        return 0
    elif n_term == 1 or n_term == 2:
        return 1
    else:
        return Fibonacci(n_term - 1) + Fibonacci(n_term - 2)
for i in range(n_term):
    print(Fibonacci(i)," ",end='')
    sum=sum+Fibonacci(i)                 # taking sum to calculate average
print("\naverage of fibonacci series is:",float(sum/n_term))

print("---------------------")
# QUESTION 8- SETS
print("     SOLUTION 8     ")
print("---------------------")
Set1={1,2,3,4,5}
Set2={2,4,6,8}
Set3={1,5,9,13,17}
print("Set1 = ", Set1)
print("Set2 = ", Set2)
print("Set3 = ", Set3)
print("(A) new set of all elements that are in Set1 and Set2 but not both")
a1=(Set1.union(Set2))-(Set1.intersection(Set2))
print(a1)
print("(B) new set of all elements that are in only one of the three sets Set1, Set2 and Set3")
b2=(Set1.union(Set2.union(Set3))) - (Set1.intersection(Set2)) - (Set1.intersection(Set3)) - (Set2.intersection(Set3))
b2=set(sorted(b2))
print(b2)
print("(C) new set of elements that are exactly two of the sets Set1, Set2 and Set3.")
c3=(Set1.intersection(Set2)).union((Set2.intersection(Set3)).union(Set1.intersection(Set3)))
print(c3)
print("(D) new set of all integers in the range 1 to 10 that are not in Set1.")
d4=set()
for i in range (1,11):
    if i not in Set1:
        d4.add(i)
d4=set(sorted(d4))
print(d4)
print("(E) new set of all integers in the range 1 to 10 that are not in Set1, Set2 and Set3.")
e5=set()
for i in range (1,11):
    if i not in Set1 and i not in Set2 and i not in Set3:
        e5.add(i)
e5=set(sorted(e5))
print(e5)
print("---------------------")
print("ASSIGNMENT 3 ENDS HERE!!!")
print("---------------------")