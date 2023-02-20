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
    print_lines()
main()