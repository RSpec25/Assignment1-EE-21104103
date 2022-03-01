# QUESTION-1 TOWER OF HANOI

def TowerOfHanoi(n, TowerA, TowerC, TowerB):         # getting values into the function
    if n == 0:
        return 0
    TowerOfHanoi(n - 1, TowerA, TowerB, TowerC)
    print("Move disk", n, "from rod", TowerA, "to rod", TowerC)
    TowerOfHanoi(n - 1, TowerB, TowerC, TowerA)


n = 3                                 # As there are 3 disk in tower a
TowerOfHanoi(n, 'A', 'C', 'B')        # passing value to function

# QUESTION-2 PASCAL TRIANGLE

from math import factorial


n = int(input('Enter the size of pascals triangle '))

print("USING WHILE LOOP")

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
print("\n\n")

print("USING RECURSSIONS")


def pascal_triangle(n, originalength=n):
    if n == 0:
        return
    pascal_triangle(n - 1, originalength)

    print('  ' * (originalength - n), end='')

    # first number is always 1
    start = 1
    for i in range(1, n + 1):
        print(start, end='   ')

        # using Binomial Coefficient
        start = start * (n - i) // i
    print()


pascal_triangle(n)
print("\n")

'''def fact(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
        i += 1
    return (fact)


n = int(input('Enter the number of rows for pascals triangle '))

print("Using Loops :-")

for i in range(n):
    for j in range(n - i + 1):
        # for spacing
        print(end=" ")

    for j in range(i + 1):
        # nCr = n!/((n-r)!*r!)
        print(fact(i) // (fact(j) * fact(i - j)), end=" ")
    # for new line
    print()
print()

print("Using Recurssion:-")


def pascal_triangle(n, originalength=n):
    if n == 0:
        return
    pascal_triangle(n - 1, originalength)
    # printing the spaces
    print('  ' * (originalength - n), end='')

    # first number is always 1
    start = 1
    for i in range(1, n + 1):
        print(start, end='   ')

        # using Binomial Coefficient
        start = start * (n - i) // i
    print()


pascal_triangle(n)
print("\n")
print("-" * 80)'''