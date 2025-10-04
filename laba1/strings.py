def select_option():
    print("1) Число слов с четным кол-вом символов \n"
          "2) Кол-во вхождений каждго символа \n"
          "3) Выход")
    option = int(input("Выберите опцию: "))
    if option == 1:
        phrase = str(input('Введите вашу фразу: \n '))
        print("Результат: " + str(count_even_length_words(phrase)))
    elif option == 2:
        phrase = str(input('Введите вашу фразу: \n '))
        print("Результат: " + str(count_frequency(phrase)))
    elif option == 3:
        return 0
    else:
        return -1
    return 1

def count_even_length_words(phrase):
    count = 0
    words = phrase.split()
    for word in words:
        if len(word) % 2 == 0:
            count += 1
    return count

def count_frequency(phrase):
    return {ch : phrase.count(ch) for ch in phrase}