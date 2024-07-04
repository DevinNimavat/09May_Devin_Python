# Write a Python program to read last n lines of a file. 

fl=open('Data_3.txt','a')
fl=open('Data_3.txt','r')

n=int(input("How many line are yout read?: "))

read=fl.readlines()[-n:]
for i in read:
    print(i)
