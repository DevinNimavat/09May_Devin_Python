s1=int(input("Enter subject 1 mark" ))
s2=int(input("Enter subject 2 mark" ))
s3=int(input("Enter subject 3 mark" ))
s4=int(input("Enter subject 4 mark" ))

total=s1+s2+s3+s4
print("total",total)

pr=total/4
print("pr",pr)

if pr>70:
    print("You are pass a+ grad")
elif pr>60:
    print("You are pass b+ grad")
elif pr>50:
    print("You are pass c grad")
elif pr>40:
    print("you are pass d grad")
else:
    print("You are fail")
