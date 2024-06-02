'''Num=int(input("Enter a Number"))

fact=1
if Num<0:
    print("This Number not Exist")
if Num ==0:
    print("This Number is 0")
if Num > 0:
    for i in range(1,Num+1):
        fact = fact * 1
    print("The number is given",fact)'''

'''n=int(input("Enter a Number"))
fact=1
for i in range(1,n+1):
  fact=fact*i
  print("Factourial")'''

'''n=int(input("Enter any number: "))
i=0
j=1
while i<n:
    i+=1
    j=j*i
print(f"Factorial Value of {n}:", j)'''

n=int(input("Enter a Number"))
a=0
b=1
c=0


for i in range(n):
  print(c,end=" ")
  c=a+b
  b=a
  a=c