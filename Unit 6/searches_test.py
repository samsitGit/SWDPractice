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

def test_linear_search_12():
    # setup
    array = [3, 5, 6, 8, 12, 17, 22, 25, 31]
    target = 12
    expected = 4

    #invoke
    result = searches.linear_search(array, target)

    #analyze
    assert result == expected

def test_linear_search_45():
    # setup
    array = [3, 5, 6, 8, 12, 17, 22, 25, 31]
    target = 45
    expected = None

    #invoke
    result = searches.linear_search(array, target)

    #analyze
    assert result == expected

def test_linear_search_6_1_4():
    # setup
    array = [3, 5, 6, 8, 12, 17, 22, 25, 31]
    target = 6
    expected = 2

    #invoke
    result = searches.linear_search(array, target, 1, 4)

    #analyze
    assert result == expected

def test_linear_search_25_3_7():
    # setup
    array = [3, 5, 6, 8, 12, 17, 22, 25, 31]
    target = 25
    expected = None

    #invoke
    result = searches.linear_search(array, target, 1, 4)

    #analyze
    assert result == expected

def test_jump_search_12():
    # setup
    array = [3, 5, 6, 8, 12, 17, 22, 25, 31]
    target = 12
    expected = 4

    #invoke
    result = searches.jump_search(array, target)

    #analyze
    assert result == expected

def test_jump_search_45():
    # setup
    array = [3, 5, 6, 8, 12, 17, 22, 25, 31]
    target = 45
    expected = None

    #invoke
    result = searches.jump_search(array, target)

    #analyze
    assert result == expected

def test_jump_search_6():
    # setup
    array = [3, 5, 6, 8, 12, 17, 22, 25, 31]
    target = 6
    expected = 2

    #invoke
    result = searches.jump_search(array, target)

    #analyze
    assert result == expected

def test_jump_search_25():
    # setup
    array = [3, 5, 6, 8, 12, 17, 22, 25, 31]
    target = 25
    expected = 7

    #invoke
    result = searches.jump_search(array, target)

    #analyze
    assert result == expected