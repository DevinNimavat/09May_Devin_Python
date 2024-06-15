# Q28. Write a Python program to remove an empty tuple(s) from a list of tuples.

list=[("a","b","d"),(5,6,26,2),(545,2351),()]

print(list)

for i in list:
    if len(i)==0:
        list.remove(i)


print(list)