# Q42. Write a Python program to print all unique values in a dictionary.

A={'A':100,'B':200,'C':300,'Q':500,'D':300}

B=[]


for i,j in A.items():
    if j not in B:
        B.append(j)

print(A)
print(B)