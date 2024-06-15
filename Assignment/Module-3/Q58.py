# Q58. Write a Python program to read a random line from a file.
import random

fr=open('line.txt','r')

R=fr.readline()

r=random.choice(R)

print(r)