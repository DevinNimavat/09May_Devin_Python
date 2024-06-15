# Q27. Write a Python program to find the repeated items of a tuple.

A=(1,2,3,4,5,6,7,8,9,0,1)

B=[]

for i in A:
    if A.count(i) >=2:
        B.append(i)

print(A)
print(tuple(set(B)))