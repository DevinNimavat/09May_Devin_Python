# Q7. Write a Python program to remove duplicates from a list. 

list=[]

list2=[]

A=int(input("Enter Your Number:"))

for  i in range(A):
    num=int(input("Enter a Any Number"))
    list.append(num)

for i in list:
    if i not in list2:
        list2.append(i)

print("Before Remove Duplicates Number in The list",list)

print("After Remove Duplicats Number in list",list2)