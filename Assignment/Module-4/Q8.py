# Write a python program to find the longest words.


fl=open('Data_3.txt')
file=fl.readlines()

max=max(file,key=len)
print(max)