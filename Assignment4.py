
# QUESTION-1 TOWER OF HANOI
print("********************")
print("     solution 1     ")
print("********************")
def TowerOfHanoi(n, TowerA, TowerC, TowerB):         # getting values into the function
    if n == 0:
        return 0
    TowerOfHanoi(n - 1, TowerA, TowerB, TowerC)
    print("Move disk", n, "from rod", TowerA, "to rod", TowerC)
    TowerOfHanoi(n - 1, TowerB, TowerC, TowerA)


n = 3                                 # As there are 3 disk in tower a
TowerOfHanoi(n, 'A', 'C', 'B')        # passing value to function
print("********************")

# QUESTION-2 PASCAL TRIANGLE
print("     solution 2     ")
print("********************")
from math import factorial


n = int(input('Enter the size of pascal triangle '))
print("USING ITERATIVE METHOD-WHILE LOOP")
i = 0
while (i < n):
    z = n - i + 1
    while (z > 0):
        print(end=" ")
        z -= 1
    y = 0
    while (y < i + 1):
        print(factorial(i) // (factorial(y) * factorial(i - y)), end=" ")
        y += 1
    i += 1
    print()
print("\n")

print("USING RECURSSIONS")
def pascal_triangle(n, originalength=n):
    if n == 0:
        return
    pascal_triangle(n - 1, originalength)
    print('  ' * (originalength - n), end='')   # printing spaces

    start = 1                                   # first number is always 1
    for i in range(1, n + 1):
        print(start, end='   ')

        start = start * (n - i) // i            # using Binomial Coefficient
    print()

pascal_triangle(n)
print("********************")

# QUESTION-3 (2 INTEGERS)
print("     solution 3     ")
print("********************")
int1, int2 = map(int, input("Enter 2 numbers with space:-").split())
Q = int1 // int2              # QUOTIENT
R = int1 % int2               # REMAINDER

# part (a)
print("PART (a)")
print("Checking if the quotient and remainder is a callable value or not.")
print(callable(Q))
print(callable(R))

# part (b)                        # finding if R and Q is zero or not
print("PART (b)")
if (Q == 0):
    print("Quotient is zero.")
if (R == 0):
    print("Remainder is zero.")
if (Q != 0 and R != 0):
    print("All of the values are non-zero.")

# part (c)
print("PART (c)")                 # adding 4 with R and Q and making list of elements that are greater with 4
list = [Q + 4, R + 4, R + 5, Q + 5, R + 5, Q + 6, R + 6]

list2 = []
for i in range(len(list)):
    if list[i] > 4:
        list2.append(list[i])
print(f"The filtered numbers that are greater than 4 are : {list2}")

# part (d)                                    # making set of list 2
print("PART (d)")
set_list2 = set(list2)
print("Set:", set_list2)

# part (e)
print("PART (e)")
immutableSet = frozenset(set_list2)           # Frozen Set makes the set immutable.
print("Immutable set:- ", immutableSet)

# part (f)
print("PART (f)")
print("Hash value of the max value from the above set:- ", hash(max(immutableSet)))
print("********************")

# QUESTION-4   CLASS
print("     solution 4     ")
print("********************")
class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno

    def _del_(self):
        print("Object deleted.")


# Creating object
student1 = Student("RISHIT SEHGAL", 21104103)
print("Object created")
# printing the assigned values
print(f"The name of the student is {student1.name} and SID is {student1.rollno}.")
# deleting object
del student1

print("********************")

# QUESTION-5  detail of 3 employees in a class
print("     solution 5     ")
print("********************")

class Employees:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

employee1 = Employees("Mehak", 40000)          #creating employee records
employee2 = Employees("Ashok", 50000)
employee3 = Employees("Viren", 60000)

print("part (a)")                    # part-(a) updating salary
employee1.salary = 70000
print(f"(a) The updated salary of {employee1.name} is {employee1.salary} ")
print("part (b)")                    # part-(b) deleting record
print("(b) Record of Viren deleted")
del employee3
print("********************")

# QUESTION-6
print("     solution 6     ")
print("********************")
# Defining anagram function
def anagram(word):
    if len(word) == 1:
        return [word]
    possible_words = anagram(word[1:])
    char = word[0]
    list1 = []
    for combination in possible_words:
        for i in range(len(combination) + 1):
            list1.append(combination[:i] + char + combination[i:])
    return list1


George_word = input("George's word:-").lower()
Barbie_word = input("Barbie's word:-").lower()
possible_words = anagram(George_word)
print("possible combinations are:", possible_words)
print("If Barbie's word is present in the list , then their friendship is real. \n")

if Barbie_word in possible_words:
    print("The Friendship is real.")
else:
    print("The Friendship is fake.")

print("*****ASSIGNMENT 4 END*****")

