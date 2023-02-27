'''
    5.2 Assignment

    Author: Sam Sit
'''

import plotter
import re
import csv

def quit():
    answer = input("Are you sure? (Y/N): ")
    if answer.lower() == "y":
        return True
    else:
        return False

def plot_grades(filename, firstname, lastname):
    with open(filename) as file:
        firstLine = ""
        for line in file:
            firstLine = line
            flSplit = firstLine.split(",")
            break
    
    #plotter.init("My Graph", "X-Axis", "Y-Axis")
    plotter.init(flSplit[0], "Students", "Grades")

    with open(filename) as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        regex = "[" + lastname + "]{" + str(len(lastname)) + "}"
        studentFound = False
        for line in csv_reader:
            print(line[0])
            if re.findall(regex, line[0]):
                print("I AM HERE")
                for number in line:
                    try:
                        plotter.add_data_point(float(number))
                    except:
                        continue
                studentFound = True
            else:
                continue

        if studentFound != True:
            return False
    
    plotter.plot()
    input("press enter to continue...")
    return True

def main():
    '''
    while True:
        command = input(">> ")
        tokens = command.split()
        try:
            if tokens[0] == "quit":
                if(quit()):
                    break
        except IndexError:
            print("Enter a command or 'quit' to quit.")

    print("Goodbye!")
    '''

    #quit()

    print(plot_grades("data/full_grades_010.csv", "Sion", "Lobasso"))
    
main()
