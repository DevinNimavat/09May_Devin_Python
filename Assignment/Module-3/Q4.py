#Write a Python function to get the largest number, smallest num and sum of all from a list.

list=[]
sum=0

A=int(input("Enter a Number: "))

for i in range(A):
    X=int(input("Enter a Intger Number:"))
    list.append(X)

max=max(list)
print("Largest Number in the List",max)

list.sort()
small=list[0]
print("Smallest Number in The list",small)

for i in list:
    sum=sum+i

print("Sum of the list Number",sum)