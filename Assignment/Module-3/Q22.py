# Q22 Write a Python program to check whether an element exists within a tuple.

A=[]

X=int(input("Enter a Number: "))

for i in range(X):
    B=int(input("Enter a Number"))
    A.append(B)

C=tuple(A)
print(C)

check=int(input("Enter a Number: "))
if check in C:
    print("Number is Exixst ")
else:
    print("Number is not exixst")
