a=input("Enter any word: ")

length=len(a)

if length < 2:
    print("")
else:
    start_char=a[:2]
    last_char=a[-2:]
    new_str=start_char + last_char
    print(new_str)