# Q45. Write a Python program to find the highest 3 values in a dictionary


A={'A':10, 'B':25, 'C':35, 'D':50, 'E':70}

B=[]

for i in A.values():
    B.append(i)

B.sort()

print("Highest 3 Value in B:",B[-3:])