# Q63. Write a Python program to returns sum of all divisors of a number

Num=int(input("Enter a Number: "))

sum=0

for i in range(1,Num):
    if Num%i ==0:
        sum+=i

print("Number is=",Num,"Sum=",sum)