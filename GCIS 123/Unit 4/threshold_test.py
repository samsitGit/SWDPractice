'''
    4.1 HW
    Author: Sam Sit
'''
def within_threshold(a, b, threshold):
    if threshold > 0:
        if (((a-b)**2)**.5) <= threshold:
            return True
        else:
            return False
    else:
        return None

def test_threshold_positive():
    assert within_threshold(1, 1, 1) == True

def test_threshold_negative():
    assert within_threshold(1, 1, -1) == None

def test_threshold_equal():
    assert within_threshold(1, 2, 1) == True

def test_threshold_false():
    assert within_threshold(1, 3, 1) == False