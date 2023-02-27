'''
    5.1 Assignment

    Author: Sam Sit
'''

def pi_tester():
    PI = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
    count = 0
    #for i in PI:
    while True:
        if count >= 100:
            break

        answer = input("Enter decimal digits of PI in order: ")
        i = PI[count+2]
        if answer == i:
            count += 1
        else:
            print("You got it wrong, the answer is", i)

def main():
    pi_tester()

main()



