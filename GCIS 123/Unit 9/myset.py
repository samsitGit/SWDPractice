def make_myset(length, hash_func=hash):
    table = []
    for i in range(length):
        table.append([])
    return (hash_func, table)

def add(myset, element):
    index = myset[0](element) % len(myset[1])
    if myset[1][index] == element:
        pass
    else:
        myset[1][index] = element

def contains(myset, element):
    index = myset[0](element) % len(myset[1])
    if myset[1][index] == element:
        return True
    else:
        return False

def main():
    a = make_myset(7)
    add(a, 5)
    add(a, 2)
    add(a, 1)
    add(a, 2)
    print(a)

    print(contains(a, 4))
    add(a,4)
    print(contains(a, 4))


main()