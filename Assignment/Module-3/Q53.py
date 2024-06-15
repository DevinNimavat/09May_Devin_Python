# Q53. How can you pick a random item from a list or tuple?


import random

A=["Rajkot","Diu","Gonal","Bhavngar","Kachh"]

B=(5,6,5,20,54,30,65,70,20)

list=random.choice(A)
Tuple=random.choice(B)

print(list)
print("Random Word Choice in= ",A,'\n')


print(Tuple)
print("Random Number Select in= ",B)