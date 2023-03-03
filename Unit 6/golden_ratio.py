'''
    6.1A The Golden Ratio HW

    Author: Sam Sit
'''
def fibonacci(n):
    n = int(n)
    if n <= 0:
        return None
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n > 2:
        return fibonacci(n-1) + fibonacci(n-2)


def main():
    n = 9
    print(fibonacci(n))

main()