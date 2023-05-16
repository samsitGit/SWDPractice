import arrays
import array_utils
import sorts

def linear_search(an_array, target):
    """
    Searches an array for a target value.
    """
    for index in range(len(an_array)):
        if an_array[index] == target:
            return index
    return None

'''
def binary_search(an_array, target, start=None, end=None):
    if start is None:
        start = 0
    if end is None:
        end = len(an_array) - 1

    if start > end:
        return None
    else:
        mid = (start + end) // 2
        # print("target =", target, "start =", start, "end =", end,
        #     "mid =", mid, "value =", an_array[mid])
        if an_array[mid] == target:
            return mid
        elif an_array[mid] < target:
            start = mid + 1
            return binary_search(an_array, target, start, end)
        else:
            end = mid - 1
            return binary_search(an_array, target, start, end)
'''

#7.11
def increasing_comparator(a, b):
    if a < b:
        return True
    return False

def decreasing_comparator(a, b):
    if a > b:
        return True
    return False

def binary_search(an_array, target, increasing_comparator, start=None, end=None):
    if start is None:
        start = 0
    if end is None:
        end = len(an_array) - 1

    if start > end:
        return None
    else:
        mid = (start + end) // 2
        # print("target =", target, "start =", start, "end =", end,
        #     "mid =", mid, "value =", an_array[mid])
        if an_array[mid] == target:
            return mid
        elif increasing_comparator(an_array[mid], target):
            start = mid + 1
            return binary_search(an_array, target, increasing_comparator, start, end)
        else:
            end = mid - 1
            return binary_search(an_array, target, increasing_comparator, start, end)

def main():
    '''
    an_array = array_utils.range_array(1, 10000001)
    print(binary_search(an_array, 1))
    print(binary_search(an_array, 5000000))
    print(binary_search(an_array, 10000000))
    print(binary_search(an_array, 0))
    #7.10
    new_array = array_utils.range_array(1, 1000)
    new_array = sorts.insertion_sort_reverse(new_array)
    print(binary_search(new_array, 50))
    print(binary_search(new_array, 250))
    print(binary_search(new_array, 500))
    print(binary_search(new_array, 750))
    #7.11
    print(increasing_comparator(1, 2))
    print(increasing_comparator(2, 1))
    print(decreasing_comparator(1, 2))
    print(decreasing_comparator(2, 1))
    '''
    #7.12
    an_array = array_utils.range_array(1, 10000001)
    print(binary_search(an_array, 1, increasing_comparator))
    print(binary_search(an_array, 5000000, increasing_comparator))
    print(binary_search(an_array, 10000000, increasing_comparator))
    print(binary_search(an_array, 0, increasing_comparator))

if __name__ == "__main__":
    main()