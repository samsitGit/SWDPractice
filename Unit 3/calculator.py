'''
    3.2 Powerpoint
    Author: Sam Sit
'''
PI = 3.14159

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def circumference(radius):
    return PI*radius*2

def area(radius):
    return PI*radius**2

def main():
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    print(add(x,y))
    print(subtract(x,y))
    print(multiply(x,y))
    print(divide(x,y))
    r = int(input("Enter radius: "))
    print(circumference(r))
    print(area(r))

main()