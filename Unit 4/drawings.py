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

    return True

def main():
    pixart.turtle.tracer(0)
    result = draw_row("01A753421")
    pixart.next_row()
    while result:
        string = input("Enter a string: ")
        result = draw_row(string)
        pixart.next_row()
    #pixart.draw_pixel_by_code("1")
    input()

main()