import random


def create_random_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        matrix.append([])
        for j in range(cols):
            matrix[i].append(random.randint(-10, 4))
    return matrix

def neg_row_sum(matrix):
    index = -1
    for row in matrix:
        neg = True
        for num in row:
            if num >= 0:
                neg = False
                break
        if neg:
            index = matrix.index(row)
            break
    if index != -1:
        return index,sum(matrix[index])
    return None, None
