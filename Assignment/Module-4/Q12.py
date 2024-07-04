# Write a Python program to copy the contents of a file to another file. 
f1=open('Data_8.txt','a')
f2=open('Data_7.txt','r')

for contents in f2:
    f1.write(contents)