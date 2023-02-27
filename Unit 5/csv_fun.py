'''
    5.21-26 lecture

    Author: Sam Sit
'''

import csv

def opener(filename):
    try:
        file = open(filename)
        file.close()
        return True
    except:
        print("File cannot be opened:", filename)
        return False

def name_and_addresses(filename):
    with open(filename) as file:
        csv_reader = csv.reader(file)
        #next(file)
        next(csv_reader)
        #for line in file:
        for line in csv_reader:
            #tokens = line.split(",")
            #print("name:", tokens[0], "address:", tokens[1])
            print("name:", line[0], "address:", line[1])

def first_only(filename):
    with open(filename) as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for line in csv_reader:
            print(line[0])

def average(filename, col):
    with open(filename) as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        sum = 0
        count = 0
        for line in csv_reader:
            number = 0
            try:
                number = float(line[int(col)])
            except:
                continue
            sum += number
            count += 1
        return sum/count
def main():
    #filename = input("Enter a file name: ")
    #print(opener(filename))
    #name_and_addresses("data/full_grades_010.csv")
    #first_only("data/full_grades_010.csv")
    #col = 3
    for col in range(3, 29):
        result = average("data/full_grades_010.csv", col)
        print(col, "average:", result)
    

main()