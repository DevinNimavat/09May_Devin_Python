# Q9. Write a Python function that takes two lists and returns true if they have at least one common member.

list=[1,2,3,4,5,6,7]
list2=[1]

Common=[]

for i in list:
    for j in list2:
        if i is j:
            Common.append(i)

if len(Common)>0:
    print("True")
else:
    print("False")