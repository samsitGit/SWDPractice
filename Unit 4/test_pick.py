'''
    4.1 Powerpoint
    Author: Sam Sit
    Must run "python -m pytest"
'''

import pick

def test_check_guess_correct():
    assert pick.check_guess(5, 5) == 0

def test_check_guess_too_high():
    assert (pick.check_guess(5, 4)) > 0

def test_check_guess_too_low():
    assert (pick.check_guess(4, 5)) > 0

if __name__ == "__main__":
    pick.main()