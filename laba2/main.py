import harmonic_series
import division
import matrix as mtrx
from polyglot import polyglot_test



if __name__ == '__main__':
    while True:
        option = int(input("Введите номер задания (0 для выхода): "))

        if option == 1:
            print(f"Результат: {harmonic_series.count_elements()}")

        elif option == 2:
            polyglot_test()
        elif option == 3:
            matrix = mtrx.create_random_matrix(5,6)
            for row  in matrix:
                print(row)
            print(f"Сумма в ряду: {mtrx.neg_row_sum(matrix)[0]} составляет: {mtrx.neg_row_sum(matrix)[1]} ")

        elif option == 4:
            a = int(input("Введите делимое: "))
            b = int(input("Введите делитель: "))
            division.divide(a,b)
        elif option == 0:
            break
        else:
            print("Неверная опция, пожалуйста повторите ваш выбор")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
