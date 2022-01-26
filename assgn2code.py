#Question 1:- STRING
str1='Python is a case sensitive language'
# 1-(a) finding length
lenstr1=len(str1)
print("length of string:",lenstr1)

# 1-(b) reversing order
print("reversed string:",str1[::-1])

# 1-(c) storing 'a case sensitive' in new string
str2=slice(10,26)
str3=str1[str2] #stored in string str3
print("stored in new string:\n",str3)

# 1-(d) replacing 'a case sensitive' with 'object oriented'
str4=str1.replace("a case sensitive","object oriented")
print("after replacing string:\n",str4)

# 1-(e) index of substring 'a'
index_1=str1.index("a")
print("index of substring 'a':",index_1)

# 1-(f) removing space from string
print("string without spaces:\n",str1.replace(" ",""))

print("\n")
#Question 2:- printing about yourself
name='Rishit Sehgal'
SID=21104103
dept='Electrical Engineering'
CGPA=9.9
print("Hey,%s Here!\nMy SID is %d\nI am from %s department and my CGPA is %s"%(name,SID,dept,CGPA))

print("\n")
#Question 3:- bitwise operator
a=56
b=10
print(a&b,"- and operator") #and operator
print(a|b,"- or operator") #or operator
print(a^b,"- xor operator") #xor operator
print(a<<2,"- left shift 2") #left shift 2
print(b<<2,"- left shift 2") #left shift 2
print(a>>2,"- right shift 2") #right shift 2
print(b>>4,"- right shift 2") #right shift 4

print("\n")
#Question 4:- greatest of three
print("Enter three no.s:")
r1=int(input())
r2=int(input())
r3=int(input())
if(r1>r2 and r1>r3):
    print("The greatest no. is:",r1)
if(r2>r1 and r2>r3):
    print("The greatest no. is:", r2)
if(r3>r1 and r3>r2):
    print("The greatest no. is:", r3)

print("\n")
#Question 5:- find word 'name'
user_string=input("Enter a string:")
if "name" in user_string:
    print("Yes")
else:
    print("No")

print("\n")
#Question 6:- valid triangle
print("Enter three side lengths of a triangle:")
side1=int(input())
side2=int(input())
side3=int(input())
if(side1+side2<side3 and side2+side3<side1 and side3+side1<side2):
    print("Yes")
print("No")

#end assignment 2**************************

