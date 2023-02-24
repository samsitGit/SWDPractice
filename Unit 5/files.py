'''
    5.2, 5.3 lecture
    command while in unit5: python files.py

    worked on split, try except, plotting, open/close files, with as,
    raise errors, re raising errors,

    problems: word search, find longest word, parse csv, 
    calculate average, etc

    Author: Sam Sit
'''
#5.2-5.3
def print_lines(filename):
    #file = open(filename)
    with open(filename) as file:
        for line in file:
            stripped = line.strip()
            #length = len(line)
            #print(length)
            print(stripped)
    #file.close()

#5.4
def word_search(filename):
    word = input("enter a word: ")
    wordLower = word.lower()
    file = open(filename)
    foundWord = False
    for line in file:
        wordToMatch = line.strip()
        if wordLower == wordToMatch:
            foundWord = True
            break #challenge
    if foundWord:
        print("The word", word, "IS found.")
    else:
        print("The word", word, "is NOT found.")
    file.close()

#5.5
def longest_word(string):
    tokens = string.split()
    longestWord = ""
    for word in tokens:
        stripped = word.strip()
        if len(stripped) == 0:
            return False
        if len(stripped) > len(longestWord):
            longestWord = stripped
    if longestWord == "":
        return False
    print("The longest word was", longestWord)

#5.5
def longest_words(filename):
    #count = 0
    file = open(filename)
    for line in file:
        longest_word(line)
        #count += 1
        #if count == 14:
            #break
    file.close()

#5.6
def print_names(filename):
    file = open(filename)
    next(file)
    for line in file:
        split =  line.split(",")
        print(split[1], split[0])
    file.close()

#5.7
def print_names(filename):
    file = open(filename)
    next(file)
    for line in file:
        split =  line.split(",")
        print(split[1], split[0])
    file.close()

def main():
    #5.2
    #print_lines("data/alice.txt")
    #5.4
    #word_search("data/words.txt")
    #5.5
    #longest_word("ham and spam")
    #longest_words("data/alice.txt")
    #5.6
    #print_names("data/grades_010.csv")
    #5.7
main()