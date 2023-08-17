def make_myset(length, hash_func=hash):
    table = []
    for i in range(length):
        table.append([])
    print(table)
    return (hash_func, table)

make_myset(5)