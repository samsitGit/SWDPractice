'''
    5.2 lecture
    Author: Sam Sit
'''

def print_lines(filename):
    file = open(filename)
    for line in file:
        length = len(line)
        print(length)
def main():
    #made my own txt file because I don't have the file from the course
    print_lines("../Unit 5/random.txt")
main()