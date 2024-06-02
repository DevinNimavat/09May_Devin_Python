a=input("Enter Your word(minimum 3 latter required): ")

length=len(a)

if length < 3:
    print(a)
elif length >= 3:
    print(a + "ing")
elif a[-3:] == "ing":
    print(a.replace("ing", "ly"))
    
