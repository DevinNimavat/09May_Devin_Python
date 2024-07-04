# Write a Python program to read first n lines of a file.

fl=open('Data_3.txt','a')
fl=open('Data_3.txt','r')

n=int(input("How many lines Areyout Read: "))

for i in range(n):
    print(fl.readline())