# Q25. Write a Python program to reverse a tuple. 

A=[]

X=int(input("Enter A Numbmer's of car:"))

for i in range(X):
    B=input("Enter A car Name:")
    A.append(B)

R=tuple(A)
a=R[::-1]

print(A)
print(a)