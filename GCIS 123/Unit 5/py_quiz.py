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

        if answer == "":
            break

        i = PI[count+2] #this is due to pi start after the dot instead of 3
        if answer == i:
            count += 1
        else:
            print("You got it wrong, the answer is", i)
    return count+1 #this is due to count starting at 0

def display_score(score):
    title = ""
    if score in range(0,5):
        title = "PI Neophyte"
    if score in range(5,10):
        title = "PI Novice"
    if score in range(10,25):
        title = "PI Journeyman"
    if score in range(25,50):
        title = "PI Enthusiast"
    if score in range(50, 97):
        title = "PI Connoisseur"
    if score in range(97,101):
        title = "PI Expert"
    if score > 100:
        title = "PI Imposter"
    print("You got a score of", score, "and is a", title)

def main():
    #pi_tester()
    display_score(pi_tester())

main()



