'''
    8.2-3 Lecture
    Author: Sam Sit
'''

def tuples(a_tuple):
    print(len(a_tuple))
    #a_tuple[0] = "b" #wont work
    for i in a_tuple:
        print(i)

def lists():
    list1 = [5, 2, "a", True]
    list1[0] = 1 #works
    for i in list1:
        print(i)
    print(list1)
    #skip 8.4

def make_list(a_sequence):
    list = []
    for i in a_sequence:
        list.append(i)
    return list

def main():
    x = ("a", 123, False)
    y = tuple("abcd")

    tuples(x)
    tuples(y)

    lists()

    print(make_list("test"))

main()