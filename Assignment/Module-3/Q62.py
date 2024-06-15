# Q62. Write a Python program to calculate surface volume and area of a cylinder.

def cylinder(radius,height):

    surface_volume=3.14*(radius*radius)*height
    surface_area=2*3.14*(radius*radius) + 2*3.14*radius*height
    print("Surface Volume of Cylinder is",surface_volume)
    print("Surface Volume of Area is", surface_area)

radius=float(input('Enter Value of Radius: '))
height=float(input('Enter Value of Height: '))

cylinder(radius,height)
