# Q16. Write a Python program to check whether a list contains a sub list


list=[1,2,5,['Devil','8'],8,]



for i in list:
    if type(i) == 'list':
        print("Yes")
    