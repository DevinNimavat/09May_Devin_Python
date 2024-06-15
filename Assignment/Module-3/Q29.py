# Q29. Write a Python program to unzip a list of tuples into individual lists. 

A=[("a","d","w","f","g"),(6,9,4,2,3,8),("Hello","Rajkot","Diu")]

count=1
for i in A:
    print(f'List {count}:{list(i)}')
    count+=1
    