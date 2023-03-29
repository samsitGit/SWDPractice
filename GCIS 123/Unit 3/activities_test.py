'''
    3.3 Powerpoint
    Author: Sam Sit
    Must run "python -m pytest"
'''

def test_square_area_8():
    value = square_area(8)
    assert value == 64

def test_square_area_6():
    value = square_area(6)
    assert value==36

def test_square_area_neg_5():
    value = square_area(-5)
    assert value == None

def square_area(length):
    #return 64
    answer = length**2
    if length < 0:
            return None
    else:
        return answer