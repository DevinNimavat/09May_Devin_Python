# Write a Python program to count the frequency of words in a file.

fl=open('Data_3.txt')
data=fl.read()

count=0
ch=input("Which charector frequency want to find?: ")

for i in data:
    if i==ch:
        count+=len(i)

print(count)