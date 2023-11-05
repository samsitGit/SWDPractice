import math 
import random

def print_board(board):
    RED = "\033[31m"
    BLACK = "\033[37m"
    
    N = len(board)
    n = math.floor(math.sqrt(N))
    assert N == n*n

    board_string = ""
    for row in range(N):
        if row > 0 and row % n == 0:
            board_string += "\n"
        for col in range(N):
            if col > 0 and col % n == 0: 
                board_string += " "
            value = board[row][col]
            if value != 0:
                board_string += RED
            else:
                board_string += BLACK
            board_string += "[{:02.0f}]".format(value)
            
        board_string += "\n" + BLACK

    print(board_string)

def random_list(start,end): #helper function to make a list of ranodmized rows to chose from
    rows=list(range(start,end))
    for i in range(0,len(rows)-1):
        j=random.randrange(i,len(rows))
        temp = rows[i]
        rows[i]=rows[j]
        rows[j]=temp
    return rows

def make_puzzle(N):
    board=[[0 for i in range(N)] for j in range(N)]

    values=range(1, N+1)

    random_row= random.randint(0,N-1)
    random_column= random.randint(0, N-1)
    for fill in values:
        while board[random_row][random_column]!=0:
            random_row= random.randint(0,N-1)
            random_column= random.randint(0, N-1)
        board[random_row][random_column]=fill

    row_sets=[]
    for index in range(0,N):
        a_set=set(board[index])
        a_set.remove(0)
        row_sets.append(a_set)

    col_sets=[]
    for i in range(0,N):
        b_set=set()
        for j in range(0,N):
            b_set.add(board[j][i]) 
        b_set.remove(0)
        col_sets.append(b_set)

    reg_sets=[]
    c_set=set()
    n=int(math.sqrt(N))
    start = 0
    for row_group in range(0,n):
        for column_group in range (0,n):
            c_set=set()
            for column in range(column_group*n, column_group*n+n):
                for row in range(row_group*n, row_group*n+n):
                    c_set.add(board[row][column])
            c_set.remove(0)
            reg_sets.append(c_set)

    #print(board)
    for i in board:
        print(i)
    #print(row_sets)
    #print(col_sets)
    for i in reg_sets:
        print(i)
    #print(reg_sets)
    # pass


def get_square(puzzle, row, col):
    pass

def move(puzzle, row, col, new_value):
    pass

def fill_puzzle(puzzle):
    pass

def main():
    N = 9
    make_puzzle(N)
    # print("Board size:", N, "x", N)
    # puzzle = make_puzzle(N)
    # print("Initial puzzle:")
    # print(puzzle)
    # print("Initial board:")
    # print_board(puzzle['board'])
    pass

     
main()
