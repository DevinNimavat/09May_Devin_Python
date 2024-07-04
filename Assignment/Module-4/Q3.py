# Write a Python program to append text to a file and display the text.

fl=open('Data_1.txt','a')
fl.write("\nMy Name is Devil...")

read=open('Data_1.txt','r')
print(read.read())
