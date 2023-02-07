'''
    Practice for functions in HW 2.2 - #4
    Author: Sam Sit
'''

def areaCircle():
    radius = float(input("Circle: r = "))
    
    print("Circle: r = ", radius, ", area = ", (3.14159*radius**2), sep="")

def volSphere():
    radius = float(input("Sphere: r = "))

    print("Sphere: r = ", radius, ", volume = ", (4/3*3.14159*radius**3), sep="")

def areaRect():
    height = float(input("Rectangle: height = "))
    width = float(input("Rectangle: width = "))
    
    print("Rectangle: height = ", height, ", width = ", width, ", area = ", (height*width), sep="")

def areaSquare():
    length = float(input("Square: side length = "))
    
    print("Square: side length = ", length, ", area = ", (length**2), sep="")

def areaIsoTri():
    side = float(input("Isosceles Triangle: side = "))
    height = float(input("Isosceles Triangle: height = "))
    
    print("Isosceles Triangle: side = ", side, ", height = ", height, ", area = ", (((side**2-height**2)**.5)*height), sep="")

def areaEqTri():
    side = float(input("Equilateral: side length = "))
    
    print("Equilateral Triangle: side = ", side, ", area = ", (((3**.5)/4)*side**2), sep="")

def areaTrap():
    base1 = float(input("Trapezoid: base 1 = "))
    base2 = float(input("Trapezoid: base 2 = "))
    height = float(input("Trapezoid: height = "))
    
    print("Trapezoid: base 1 = ", base1, ", base 2 = ", base2, ", height = ", height, ", area = ", (((base1+base2)/2)*height), sep="")

def main():
    areaCircle()
    volSphere()
    areaRect()
    areaIsoTri()
    areaEqTri()
    areaTrap()

main()