'''
    5.21 lecture

    Author: Sam Sit
'''

def opener(filename):
    try:
        file = open(filename)
        file.close()
        return True
    except:
        print("File cannot be opened:", filename)
        return False
    
def main():
    filename = input("Enter a file name: ")
    print(opener(filename))

main()