a=int(input("Enter a Number"))
b=int(input("Enter a Second Number"))

print("Enter 1 for sum")
print("Enter 4 for sub")
print("Enter 3 for mul")
print("Enter 2 for div")

c=int(input("Enter your Choice")) 

if c==1:
    print("Add",a+b)
elif c==2:
    print("Sub",a-b)
elif c==3:
    print("Mul",a*b)
elif c==4:
    print("Div",a/b)
else:
    print("Error")

