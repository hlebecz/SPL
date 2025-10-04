from itertools import count


def count_elements(goal = 4):
    summ = 0
    for el in count(1):
        summ += 1/el
        if summ > goal:
            print(el, summ)
            return el
    return None
