'''
    8 Lecture
    Author: Sam Sit
'''

def make_board():
    t = []
    v = " "
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

def make_move(b, s):
    r = int(input("Enter a row (1-3): "))
    c = int(input("Enter a col (1-3): "))

    while not b[r-1][c-1] == " ":
        print("Please retry:")
        r = int(input("Enter a row (1-3): "))
        c = int(input("Enter a col (1-3): "))

    b[r-1][c-1] = s
    print_board(b)

def main():
    #print_board(make_board())
    b = make_board()
    print_board(b)
    for i in range(9):
        if i % 2:
            make_move(b, "O")
        else:
            make_move(b, "X")
    print("The game is over!")

main()