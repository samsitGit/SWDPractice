'''
    9 lecture
    Author: Sam Sit
'''

def make_student(id, name):
    credit = 0
    gpa = 0
    return [id, name, credit, gpa]

def add_student(population, id, name):
    index = 0
    for a in population:
        if id == a[0]:
            population.pop(index)
        index += 1
    population.append(make_student(id, name))

def get_student(population, id):
    for i in population:
        if id == i[0]:
            return i
        else:
            return None

def add_credits(population, id, credits):
    s = get_student(population, id)
    if s != None:
        s[2] += credits

def get_credits(population, id):
    s = get_student(population, id)
    if s != None:
        return s[2]
    else:
        return None

def main():
    '''
    s1 = make_student(1, "Sam Sit")
    s2 = make_student(2, "Sun Sit")
    s3 = make_student(3, "San Sit")
    s4 = make_student(4, "Sin Sit")
    print(s1)
    print(s2)
    print(s3)
    print(s4)
    '''
    population = []

    add_student(population, 1, "Sam Sit")
    add_student(population, 2, "Sun Sit")
    add_student(population, 3, "San Sit")
    add_student(population, 4, "Sin Sit")
    '''
    print(get_student(population, 1))
    print(get_student(population, 6))
    '''
    add_credits(population, 1, 50)
    print(get_credits(population, 1))


main()