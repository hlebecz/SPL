""" . Напишите функцию, которая будет принимать один аргумент. Если в
функцию передаётся список, удалить все повторяющиеся элементы. Найти в
новом списке сумму после первого положительного элемента.
Если словарь – отсортировать в порядке убывания по значению.
Число – определить простое, или нет.
Строка – каждый символ перевести в соответствующий ему код из
таблицы символов Unicode.
Сделать проверку со всеми этими случаями."""

def polyglot(arg):
    if isinstance(arg, list):
        new_list = []
        # не используется list(set()) потому что важен порядок чисел
        for i in arg:
            if i not in new_list:
                new_list.append(i)
        for i in range(len(new_list)):
            if new_list[i] > 0:
                new_list = new_list[i:]
                print(new_list)
                return sum(new_list)
        return None

    elif isinstance(arg, str):
        return [ord(char) for char in arg]

    elif isinstance(arg, int):
        return is_prime(arg)

    elif isinstance(arg, dict):
        return sorted(arg, key=arg.get, reverse=True)

    else :
        return None


def polyglot_test():
    while True:
        print("\nВыберите тип данных для тестирования:")
        print("1. Список (list)")
        print("2. Строка (str)")
        print("3. Целое число (int)")
        print("4. Словарь (dict)")
        print("5. Выход")

        choice = input("Введите номер варианта (1-5): ")

        if choice == '1':
            print("Тестирование со списком ")
            try:
                user_input = input("Введите числа через пробел: ")
                numbers = [int(x.strip()) for x in user_input.split()]
                print(f"Входные данные: {numbers}")
                result = polyglot(numbers)
                print(f"Результат: {result}")
            except ValueError:
                print("Ошибка: введите корректные числа!")

        elif choice == '2':
            print("Тестирование со строкой")
            user_input = input("Введите строку: ")
            print(f"Входные данные: '{user_input}'")
            result = polyglot(user_input)
            print(f"Коды символов: {result}")

        elif choice == '3':
            print("Тестирование с целым числом ")
            try:
                user_input = int(input("Введите целое число: "))
                print(f"Входные данные: {user_input}")
                result = polyglot(user_input)
                print(f"Является ли простым числом: {result}")
            except ValueError:
                print("Ошибка: введите корректное целое число!")

        elif choice == '4':
            print("Тестирование со словарем ")
            try:
                print("Введите пары ключ-значение в формате: ключ1:значение1,ключ2:значение2")
                user_input = input("Например: a:5,b:2,c:8,d:1: ")

                pairs = [pair.strip() for pair in user_input.split(',')]
                dictionary = {}

                for pair in pairs:
                    if ':' in pair:
                        key, value = pair.split(':', 1)
                        dictionary[key.strip()] = int(value.strip())

                print(f"Входные данные: {dictionary}")
                result = polyglot(dictionary)
                print(f"Ключи, отсортированные по значениям (по убыванию): {result}")
            except ValueError:
                print("Ошибка: введите корректные пары ключ-значение!")

        elif choice == '5':
            break

        else:
            print("Неверный выбор. Пожалуйста, введите число от 1 до 5.")

def is_prime(n: int):
    if n < 2:
        return False
    for i in range(2, n // 2):
        if n % i == 0:
            return False
    return True
