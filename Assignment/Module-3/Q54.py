# Q54. How can you pick a random item from a range?

import random

def Random(num1,num2):
    Num_R=random.choice(range(num1,num2))
    print(f"Randome Number from Range Between {num1} and {num2} is {Num_R}")


S_N=int(input("Enter a Frist Number: "))
L_N=int(input("Enter a Sencond Number: "))

Random=(S_N,L_N)
