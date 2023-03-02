'''
    6.9 lecture

    Author: Sam Sit
'''
import arrays
import arrays_utils

def linear_search(an_array, target):
    count = 0
    for i in range(len(an_array)):
        if an_array[count] == target:
            print("found", target)
            return count
        count += 1
    print("did not find", target)
    return None

def main():
    array = arrays_utils.range_array(1,100)
    target = 50
    print(linear_search(array, target))

main()