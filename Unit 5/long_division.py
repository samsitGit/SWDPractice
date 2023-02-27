'''
    5.1 Assignment

    Author: Sam Sit
'''

def precise_divison(n, d, p):
    n = int(n)
    d = int(d)
    p = int(p)
    
    return str(round((d/n),p))

def main():
    #print(precise_divison(25, 425, 25))
    print(precise_divison(2, 7, 25))
    '''
    para = input("Enter division parameters: ")
    tokens = para.split(" ")
    num = tokens[0]
    den = tokens[1]
    pre = tokens[2]
    print(precise_divison(num, den, pre))
    '''

main()
