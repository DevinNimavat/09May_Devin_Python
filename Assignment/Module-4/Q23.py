'''Write a Python class named Rectangle constructed by a length and 
width and a method which will compute the area of a rectangle'''

class rectangle:

    def Ans():
        lengh=int(input("Enter Number of Lengh: "))
        width=int(input("Enter Number of Width: "))

        area=lengh*width

        print("Your Answer is:",area)

r=rectangle()
r.Ans()