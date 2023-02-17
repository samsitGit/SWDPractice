'''
    4.2 HW
    Author: Sam Sit
'''

import pixart

def len(string):
    count = 0
    for x in string:
        count += 1
    return count


def draw_row(string):
    length = len(string)
    if length == 0:
        return False

    count = 0
    while count < length:
        color = string[count]
        if pixart.decoder(color) == False:
            return False
        else:
            pixart.draw_pixel_by_code(color)
        count = count + 1

def 

def main():
    draw_row("01A753421")
    #pixart.draw_pixel_by_code("1")
    input()

main()