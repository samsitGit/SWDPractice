'''
    5.3 Assignment

    Author: Sam Sit
'''

import plotter
import re
import csv

def plot_grades(filename, first_name, last_name):

    with open(filename) as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        regex = ".*" + last_name + ".*" + first_name + ".*"
        studentFound = False
        for line in csv_reader:
            if re.findall(regex, line[0]):
                count = 0
                plotter.init((first_name + " " + last_name), "Grade Item", "Scores")
                studentFound = True
                for number in line:
                    count += 1
                    if count > 3: #skip first 3 columns
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

def get_average(filename, column):
            
    with open(filename) as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        sum = 0
        count = 0
        for line in csv_reader:
            try:
                sum += float(line[column])
                count += 1
            except ValueError:
                continue

    return round(sum/count, 2)

def plot_class_averages(filename):
    plotter.init("Class average", "Grade Item", "Scores")
    for i in range(3, 30):
        plotter.add_data_point(float(get_average(filename, i)))
    plotter.plot()
                               

def main():

    #print(plot_grades("data/full_grades_010.csv", "Sion", "Lobasso"))
    #print(get_average("data/full_grades_010.csv", 5))
    plot_class_averages("data/full_grades_010.csv")
    input()

main()
