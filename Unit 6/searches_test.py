'''
    6.2A HW

    Author: Sam Sit
'''
import arrays_utils
import searches

def test_linear_search():
    # setup
    array = arrays_utils.range_array(1,100)
    target = 50
    expected = 49

    #invoke
    result = searches.linear_search(array, target)

    #analyze
    assert result == expected

def test_linear_search_out():
    # setup
    array = arrays_utils.range_array(1,100)
    target = 101

    #invoke
    try:
        result = searches.linear_search(array, target)
        assert False

    #analyze
    except:
        assert True

def test_linear_search_min():
    # setup
    array = arrays_utils.range_array(1,100)
    target = 1
    expected = 0

    #invoke
    result = searches.linear_search(array, target)

    #analyze
    assert result == expected

def test_linear_search_max():
    # setup
    array = arrays_utils.range_array(1,100)
    target = 100
    expected = 99

    #invoke
    result = searches.linear_search(array, target)

    #analyze
    assert result == expected

def test_binary_search():
    # setup
    array = arrays_utils.range_array(1,100)
    target = 50
    expected = 49

    #invoke
    result = searches.binary_search(array, target)

    #analyze
    assert result == expected

def test_binary_search_out():
    # setup
    array = arrays_utils.range_array(1,100)
    target = 101

    #invoke
    try:
        result = searches.binary_search(array, target)
        assert False

    #analyze
    except:
        assert True

def test_binary_search_min():
    # setup
    array = arrays_utils.range_array(1,100)
    target = 1
    expected = 0

    #invoke
    result = searches.binary_search(array, target)

    #analyze
    assert result == expected

def test_binary_search_max():
    # setup
    array = arrays_utils.range_array(1,100)
    target = 100
    expected = 99

    #invoke
    result = searches.binary_search(array, target)

    #analyze
    assert result == expected

