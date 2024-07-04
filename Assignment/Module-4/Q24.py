'''Write a Python class named Circle constructed by a radius and two 
methods which will compute the area and the perimeter of a circle '''

class circle:
    def area(self):
        pi=3.14

        reduis=int(input("Enter Number reduis: "))

        a=pi*(reduis*reduis)

        print("Aera of circle: ",a)

    def perameter(self):

        pi=3.14

        x=int(input("Enter Number o Reduis: "))

        y=2*pi*x

        print("Perimeter of Cyrcle is: ",y)

C=circle()
C.area()
C.perameter()


