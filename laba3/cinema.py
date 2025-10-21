def read_movies(filename):
    movies = []

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            parts = line.split()
            movie_name_parts = []
            date_index = -1

            for i, part in enumerate(parts):
                if all(c in '0123456789.' for c in part):
                    date_index = i
                    break
                movie_name_parts.append(part)

            if date_index == -1 or date_index + 2 >= len(parts):
                print(f"Ошибка в формате строки: {line}")
                continue

            # Собираем данные
            movie_name = ' '.join(movie_name_parts)
            date = parts[date_index]
            price = float(parts[date_index + 1])
            viewers = int(parts[date_index + 2])

            movies.append({
                'name': movie_name,
                'date': date,
                'price': price,
                'viewers': viewers
            })

    return movies


def print_movies_cheaper_than(movies, max_price):
    print(f"\nФильмы стоимостью меньше {max_price} рублей:")

    found = False
    for movie in movies:
        if movie['price'] < max_price:
            print(f"{movie['name']} - {movie['price']} руб. ({movie['date']})")
            found = True

    if not found:
        print("Фильмы не найдены")


def print_movies_by_date(movies, target_date):
    print(f"\nФильмы за дату {target_date}:")

    found = False
    for movie in movies:
        if movie['date'] == target_date:
            print(f"{movie['name']} - {movie['price']} руб. (зрителей: {movie['viewers']})")
            found = True

    if not found:
        print("Фильмы не найдены")

def print_all_movies(movies):
    for movie in movies:
        print(f"{movie['name']} - {movie['price']} руб. ({movie['date']}) (зрителей: {movie['viewers']})")

def select_option():
    while True:
        print("1) Фильмы стоимостью менее 15 руб. \n"
              "2) Фильмы на определенную дату \n"
              "3) Выход")
        option = int(input("Выберите опцию: "))
        if option == 1:
            print_movies_cheaper_than(read_movies("Кинотеатр.txt"), 15)
        elif option == 2:
            date = input("Введите вашу дату в формате ДД.ММ.ГГГГ:")
            print_movies_by_date(read_movies("Кинотеатр.txt"), date)
        elif option == 3:
            return 0
        else:
            return -1
