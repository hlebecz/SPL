def min_even(numbers: tuple):
    even_numbers = [num for num in numbers if num % 2 == 0]
    if len(even_numbers) != 0:
        return min(even_numbers)
    else:
        return 0


