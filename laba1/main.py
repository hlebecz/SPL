import strings
import pairs
import store
import min_even
import chinese

if __name__ == '__main__':
    option = -1
    while option != 0:

        option = int(input("Введите номер задания (0 для выхода): "))

        if option == 1:
            chinese.enable()
        elif option == 2:
            while 1:
                status = strings.select_option()
                if status == 0:
                    break

        elif option == 3:
            ls = pairs.generate_random_list(10,5)
            print("Список: " + str(ls))
            print("Результат: " + str(pairs.count_pairs(ls)))

        elif option == 4:
            my_dict = {'a': 111, 'b': 122, 'c': 566, 'd': 405, 'e': 21, 'f': 266}
            print(my_dict)
            for i in range(0,3):
                res = max(my_dict, key=my_dict.get)
                print(" " + str(res))
                del my_dict[res]

        elif option == 5:
            store.start_store()

        elif option == 6:
            tpl = tuple(pairs.generate_random_list(10,100))
            print("Кортеж: " + str(tpl))
            print("Результат: " + str(min_even.min_even(tpl)))

        elif option == 0:
            break

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
