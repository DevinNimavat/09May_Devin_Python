# Q51.Write a Python function that checks whether a passed string is palindrome or not

def Palindrome_Str(str):
    if str == str[::-1]:
        print("This String palindrome Number: ",str)
    else:
        print("This String palindrome Not Number: ",str)

str=input("Enter a String: ")

Palindrome_Str(str)