'''
    5.19-20 lecture

    Author: Sam Sit
'''

import activities

def test_exponent():
    assert activities.exponent(2, 2) == 4
    assert activities.exponent(10, 2) == 100

def test_raiseValueError():
    #set up
    base = 3
    power = -1

    #invoke
    try: 
        activities.exponent(base, power)
        assert False
    
    #analyze
    except ValueError:
        assert True