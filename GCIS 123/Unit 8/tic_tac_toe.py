'''
    8 Lecture
    Author: Sam Sit
'''

def make_board():
    t = []
    v = "0"
    for i in range(3):
        r = []
        for j in range(3):
            r.append(v)
        t.append(r)
    return t

def print_board(b):
    for i in range(len(b)):
        for j in range(len(b)):
            if j == len(b)-1:
                print(b[i][j])
            else:
                print(b[i][j], end = "|")
        if not i == len(b)-1:
            print("-----")

def main():
    print_board(make_board())

main()