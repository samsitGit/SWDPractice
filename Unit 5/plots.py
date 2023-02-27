'''
    5.2 Assignment

    Author: Sam Sit
'''

def quit():
    answer = input("Are you sure? (Y/N): ")
    if answer.lower() == "y":
        return True
    else:
        return False


def main():
    while True:
        command = input(">> ")
        tokens = command.split()
        if tokens[0] == "quit":
            if(quit()):
                break
    print("Goodbye!")
    
    #quit()
    
main()
