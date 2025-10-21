from datetime import datetime
import os


class Cinema:

    def __init__(self, filename: str = "Кинотеатр.txt") -> None:
        self.filename = filename
        self.movies: list[dict] = []
        self._load_movies()

    def _load_movies(self) -> None:
        if not os.path.exists(self.filename):
            print(f"Файл {self.filename} не найден!")
            return

        self.movies = []
        with open(self.filename, 'r', encoding='utf-8') as file:
            for line_num, line in enumerate(file, 1):
                line = line.strip()
                if not line:
                    continue

                try:
                    movie_data = self._parse_movie_line(line, line_num)
                    if movie_data:
                        self.movies.append(movie_data)
                except Exception as e:
                    print(f"Ошибка в строке {line_num}: {e}")

    def _parse_movie_line(self, line: str, line_num: int) -> dict | None:
        parts = line.split()
        movie_name_parts = []
        date_index = -1

        for i, part in enumerate(parts):
            if self._is_date(part):
                date_index = i
                break
            movie_name_parts.append(part)

        if date_index == -1 or date_index + 2 >= len(parts):
            print(f"Ошибка в формате строки {line_num}: {line}")
            return None

        movie_name = ' '.join(movie_name_parts)
        date = parts[date_index]
        price = float(parts[date_index + 1])
        viewers = int(parts[date_index + 2])

        return {
            'name': movie_name,
            'date': date,
            'price': price,
            'viewers': viewers
        }



    # МЕТОДЫ ЭКЗЕМПЛЯРА
    def get_movies_cheaper_than(self, max_price: float) -> list[dict]:
        return [movie for movie in self.movies if movie['price'] < max_price]

    def get_movies_by_date(self, target_date: str) -> list[dict]:
        return [movie for movie in self.movies if movie['date'] == target_date]

    def get_movies_by_name(self, name_part: str) -> list[dict]:
        return [movie for movie in self.movies
                if name_part.lower() in movie['name'].lower()]

    def get_most_popular_movie(self) -> dict | None:
        if not self.movies:
            return None
        return max(self.movies, key=lambda x: x['viewers'])

    def get_total_revenue(self) -> float:
        return sum(movie['price'] * movie['viewers'] for movie in self.movies)

    def get_average_price(self) -> float:
        if not self.movies:
            return 0.0
        return sum(movie['price'] for movie in self.movies) / len(self.movies)

    def add_movie(self, name: str, date: str, price: float, viewers: int) -> None:
        if not self._is_date(date):
            raise ValueError("Неверный формат даты. Используйте ДД.ММ.ГГГГ")

        new_movie = {
            'name': name,
            'date': date,
            'price': price,
            'viewers': viewers
        }

        self.movies.append(new_movie)
        self._save_to_file()
        print(f"Фильм '{name}' успешно добавлен!")

    def remove_movie(self, name: str, date: str) -> bool:
        initial_count = len(self.movies)
        self.movies = [movie for movie in self.movies
                       if not (movie['name'] == name and movie['date'] == date)]

        if len(self.movies) < initial_count:
            self._save_to_file()
            print(f"Фильм '{name}' за {date} удален!")
            return True
        else:
            print(f"Фильм '{name}' за {date} не найден!")
            return False

    def _save_to_file(self) -> None:
        with open(self.filename, 'w', encoding='utf-8') as file:
            for movie in self.movies:
                line = f"{movie['name']} {movie['date']} {movie['price']} {movie['viewers']}\n"
                file.write(line)

    # СТАТИЧЕСКИЕ МЕТОДЫ
    @staticmethod
    def _is_date(text: str) -> bool:
        try:
            if '.' in text and len(text.split('.')) == 3:
                day, month, year = text.split('.')
                if len(day) == 2 and len(month) == 2 and len(year) == 4:
                    datetime.strptime(text, '%d.%m.%Y')
                    return True
        except ValueError:
            pass
        return False

    @staticmethod
    def format_movie_info(movie: dict) -> str:
        return (f"{movie['name']} | {movie['date']} | "
                f"{movie['price']} руб. | {movie['viewers']} зрителей")

    @staticmethod
    def validate_price(price: float) -> bool:
        return price >= 0

    # МЕТОД КЛАССА
    @classmethod
    def create_sample_cinema(cls) -> 'Cinema':
        filename = "sample_cinema.txt"
        sample_data = [
            "Интерстеллар 15.10.2023 12.5 150",
            "Аватар 16.10.2023 15.0 200",
            "Начало 15.10.2023 10.0 100",
            "Криминальное чтиво 17.10.2023 8.5 80",
            "Побег из Шоушенка 16.10.2023 11.0 120"
        ]

        with open(filename, 'w', encoding='utf-8') as f:
            for line in sample_data:
                f.write(line + '\n')

        return cls(filename)

    def __str__(self) -> str:
        return f"Кинотеатр: {len(self.movies)} фильмов, выручка: {self.get_total_revenue():.2f} руб."

    def __len__(self) -> int:
        return len(self.movies)

    def __getitem__(self, index: int) -> dict:
        return self.movies[index]


class CinemaManager:
    def __init__(self, cinema: Cinema) -> None:
        self.cinema = cinema

    def display_menu(self) -> None:
        print("УПРАВЛЕНИЕ КИНОТЕАТРОМ")
        print("1) Фильтр фильмов по стоимости")
        print("2) Фильмы на определенную дату")
        print("3) Найти фильм по названию")
        print("4) Самый популярный фильм")
        print("5) Статистика кинотеатра")
        print("6) Добавить фильм")
        print("7) Удалить фильм")
        print("8) Показать все фильмы")
        print("9) Выход")

    def run(self) -> None:
        while True:
            self.display_menu()
            try:
                option = int(input("Выберите опцию: "))

                if option == 1:
                    self._show_cheap_movies()
                elif option == 2:
                    self._show_movies_by_date()
                elif option == 3:
                    self._search_movies_by_name()
                elif option == 4:
                    self._show_most_popular()
                elif option == 5:
                    self._show_statistics()
                elif option == 6:
                    self._add_movie()
                elif option == 7:
                    self._remove_movie()
                elif option == 8:
                    self._show_all_movies()
                elif option == 9:
                    print("До свидания!")
                    break
                else:
                    print("Неверная опция! Попробуйте снова.")

            except ValueError:
                print("Пожалуйста, введите число!")
            except Exception as e:
                print(f"Произошла ошибка: {e}")

    def _show_cheap_movies(self) -> None:
        max_price = float(input("Введите максимальную цену: "))
        movies = self.cinema.get_movies_cheaper_than(max_price)

        print(f"\nФильмы стоимостью меньше {max_price} рублей:")
        if movies:
            for movie in movies:
                print(f"  - {Cinema.format_movie_info(movie)}")
        else:
            print("  Фильмы не найдены")

    def _show_movies_by_date(self) -> None:
        date = input("Введите дату в формате ДД.ММ.ГГГГ: ")
        movies = self.cinema.get_movies_by_date(date)

        print(f"\nФильмы за дату {date}:")
        if movies:
            for movie in movies:
                print(f"  - {Cinema.format_movie_info(movie)}")
        else:
            print("  Фильмы не найдены")

    def _search_movies_by_name(self) -> None:
        name_part = input("Введите часть названия фильма: ")
        movies = self.cinema.get_movies_by_name(name_part)

        print(f"\nФильмы содержащие '{name_part}':")
        if movies:
            for movie in movies:
                print(f"  - {Cinema.format_movie_info(movie)}")
        else:
            print("  Фильмы не найдены")

    def _show_most_popular(self) -> None:
        movie = self.cinema.get_most_popular_movie()
        if movie:
            print(f"\nСамый популярный фильм:")
            print(f"  - {Cinema.format_movie_info(movie)}")
        else:
            print("Нет данных о фильмах")

    def _show_statistics(self) -> None:
        print(f"\nСтатистика кинотеатра:")
        print(f"  Всего фильмов: {len(self.cinema)}")
        print(f"  Общая выручка: {self.cinema.get_total_revenue():.2f} руб.")
        print(f"  Средняя цена билета: {self.cinema.get_average_price():.2f} руб.")

    def _add_movie(self) -> None:
        name = input("Название фильма: ")
        date = input("Дата (ДД.ММ.ГГГГ): ")
        price = float(input("Цена билета: "))
        viewers = int(input("Количество зрителей: "))

        self.cinema.add_movie(name, date, price, viewers)

    def _remove_movie(self) -> None:
        name = input("Название фильма: ")
        date = input("Дата (ДД.ММ.ГГГГ): ")

        self.cinema.remove_movie(name, date)

    def _show_all_movies(self) -> None:
        print(f"\nВсе фильмы ({len(self.cinema)}):")
        for i, movie in enumerate(self.cinema.movies, 1):
            print(f"{i:2d}. {Cinema.format_movie_info(movie)}")
