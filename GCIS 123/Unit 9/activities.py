'''
    9 lecture
    Author: Sam Sit
'''

def unique_array(a, v):
    noneIndex = None
    noneIndexFound = False
    for i in range(len(a)):
        if a[i] == None and not noneIndexFound:
            noneIndex = i
            noneIndexFound = True
        elif a[i] == v:
            return
    a[noneIndex] = v