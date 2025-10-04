from random import randint

def count_pairs(numbers):
    pairs_count = {}
    num_count = { num : numbers.count(num) for num in numbers }

    for num, count in num_count.items():
        if count > 1:
            pairs_count[num] = count * (count - 1) / 2
    return pairs_count


def generate_random_list(length: int, border: int):
    return [randint(1, border) for i in range(length)]