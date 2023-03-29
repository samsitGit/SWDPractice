"""
This program prints a hello world and customized message to the user.
Author: Sam Sit
"""

def helloWorld(): #define function
    print("Hello, World!") #prints string

def helloYou(): #define function
    name = input("What is your name? :") #print, ask for input, and save in variable
    print("Hello, ", name, "!", sep="") #prints string formatted

helloWorld() #runs the first function
helloYou() #runs the second function