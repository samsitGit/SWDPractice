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
        try:
            if tokens[0] == "quit":
                if(quit()):
                    break
        except IndexError:
            print("Enter a command or 'quit' to quit.")
            
    print("Goodbye!")

    #quit()
    
main()
