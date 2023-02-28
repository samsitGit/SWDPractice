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
    
    ''' # to get first line
    with open(filename) as file:
        firstLine = ""
        for line in file:
            firstLine = line
            flSplit = firstLine.split(",")
            break
    '''

    #plotter.init("My Graph", "X-Axis", "Y-Axis")
    #plotter.init(flSplit[0], "Scores", "Grades")

    with open(filename) as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        #regex = "[" + lastname + "]{" + str(len(lastname)) + "}\w[" + firstname + "]{" + str(len(firstname)) + "}"
        #regex = ".*Lobasso.*Sion.*"
        studentFound = False
        for line in csv_reader:
            #if re.findall(regex, line[0]):
            if line[0] == lastname and line[1] == firstname:
                count = 0
                plotter.init((firstname + " " + lastname), "Scores", "Grades")
                studentFound = True
                for number in line:
                    count += 1
                    if count > 2: #skip first 2 columns
                        try:
                            plotter.add_data_point(float(number))
                        except ValueError:
                            plotter.add_data_point(0)

            else:
                continue

        if studentFound != True:
            return False
        else:
            plotter.plot()
            input("press enter to continue...")
            return True

def student_grades(string):
    tokens = string.split(" ")
    try:
        command = tokens[0]
        filename = tokens[1]
        firstname = tokens[2]
        lastname = tokens[3]
        if command == "stu":
            if plot_grades(filename, firstname, lastname):
                print("Plot finished (window may be hidden).")
            else:
                print("Plot failed, (no such student).")
        else:
            print("Command should be stu")
    except IndexError:
        print("Usage: stu <filename> <first name> <last name>")
    except FileNotFoundError:
        print("No such file:", filename)
    
def help():
    print("stu <filename> <first name> <last name> - plot student grades")
    print("cavg <filename> - plot class average")
    print("avg <filename> <number> - prints the average for the grade item")
    print("quit - quits")
    print("help - displays this message")

def main():
    #'''
    while True:
        command = input(">> ")
        tokens = command.split()
        try:
            if tokens[0] == "quit":
                if(quit()):
                    break
            elif tokens[0] == "stu":
                student_grades(command)
            elif tokens[0] == "help":
                help()
        except IndexError:
            print("Enter a command or 'quit' to quit.")

    print("Goodbye!")
    #'''
    #plot_grades("data/grades_010.csv", "asd", "lastname")

    #quit()
    #print(plot_grades("data/grades_010.csv", "Sion", "Lobasso"))
    #student_grades("stu data/grades_010.csv Sion Lobasso")
    #student_grades("stu data/grades_010.csv Sion")
    #student_grades("stu data/gradasdasdes_010.csv Sion Lobasso")

    #print(plot_grades("data/full_grades_010.csv", "Sion", "Lobasso"))
    #print(plot_grades("data/full_grades_010.csv", "Carlyne", "Myrman"))
    
main()
