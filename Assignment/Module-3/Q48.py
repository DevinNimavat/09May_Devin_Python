# Q48. Write a Python function to calculate the factorial of a number (anonnegative integer) 

def Factorial(N):
    count = 1

    if N<0:
        print("Number is Negative........ Pleace Enter Positive Number")
    elif N == 0:
        print("Number Is ZERO....")

    elif N >=0:


        for i in range(1,N+1):
            count *=i

        print("Number is= ",N,"Factorial Is= ",count)

A=int(input("Enter a Number For Find FActorial: "))

Factorial(A)