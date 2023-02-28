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

    print("average:", sum/count)

def main():

    #print(plot_grades("data/full_grades_010.csv", "Sion", "Lobasso"))
    for i in range(3, 30):
        get_average("data/full_grades_010.csv", i)
    
main()
