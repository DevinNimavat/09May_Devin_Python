# Q10. Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30.

F_5=[]
L_5=[]

for i in range(1,31):
    if i<=5:
        S=i*i
        F_5.append(S)

    if i>25:
        s=i*i
        L_5.append(s)

print(F_5)
print(L_5)