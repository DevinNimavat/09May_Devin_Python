# Q24. Write a Python program to convert a list to a tuple.

A=[]

B=int(input("Enter Number of City: "))

for i in range(B):
    City=input("Enter Your City Name: ")
    A.append(City)
    B=tuple(A)

print("Without Converting to Tuple",A)
print("Converting In Tuple",B)