class Country:
    def __init__(self, name: str, capital: str, area: float, population: int) -> None:
        self.name = name
        self.capital = capital
        self.area = area
        self.population = population

    def __str__(self) -> str:
        return (f"{self.name} ->"
                f"Столица: {self.capital} "
                f"Площадь: {self.area} "
                f"Население: {self.population}"
                )


class CountryManipulator:
    def __init__(self, countries: list[Country]) -> None:
        self.countries = countries.copy()

    def filter_by_area(self, min_area: float = 0, max_area: float = None) -> list[Country]:
        if max_area is None:
            max_area = float('inf')

        return list(filter(lambda c: min_area <= c.area <= max_area, self.countries))

    def filter_by_population(self, min_pop: int = 0, max_pop: int = None) -> list[Country]:
        if max_pop is None:
            max_pop = int('inf')

        return list(filter(lambda c: min_pop <= c.area <= max_pop, self.countries))

    def print_countries(self):
        for c in self.countries:
            print(c)


def select_option():
    countries = [
        Country("Россия", "Москва", 17125191, 146000000),
        Country("Германия", "Берлин", 357022, 83000000),
        Country("Франция", "Париж", 643801, 68000000),
        Country("Великобритания", "Лондон", 243610, 67000000),
        Country("Италия", "Рим", 301340, 59000000),
        Country("Испания", "Мадрид", 505990, 47000000),
        Country("Украина", "Киев", 603628, 41000000),
        Country("Польша", "Варшава", 312679, 38000000),
        Country("Канада", "Оттава", 9984670, 38000000),
        Country("США", "Вашингтон", 9833517, 331000000),
        Country("Китай", "Пекин", 9596961, 1400000000),
        Country("Индия", "Нью-Дели", 3287263, 1380000000),
        Country("Япония", "Токио", 377975, 125000000),
        Country("Бразилия", "Бразилиа", 8514877, 213000000),
        Country("Австралия", "Канберра", 7692024, 25600000),
        Country("Мексика", "Мехико", 1964375, 126000000),
        Country("Южная Корея", "Сеул", 100210, 51000000),
        Country("Турция", "Анкара", 783562, 84000000),
        Country("Египет", "Каир", 1001449, 104000000),
        Country("ЮАР", "Претория", 1221037, 60000000),
        Country("Аргентина", "Буэнос-Айрес", 2780400, 45000000),
        Country("Норвегия", "Осло", 385207, 5400000),
        Country("Швеция", "Стокгольм", 450295, 10300000),
        Country("Финляндия", "Хельсинки", 338424, 5500000),
        Country("Нидерланды", "Амстердам", 41543, 17000000),
        Country("Бельгия", "Брюссель", 30528, 11500000),
        Country("Швейцария", "Берн", 41285, 8700000),
        Country("Австрия", "Вена", 83879, 8900000),
        Country("Греция", "Афины", 131990, 10400000),
        Country("Португалия", "Лиссабон", 92090, 10300000)
    ]

    country_manipulator = CountryManipulator(countries)
    while True:
        print("1) Показать все страны \n"
              "2) Фильтр по площади \n"
              "3) Фильтр по населению \n"
              "4) Выход")
        option = int(input("Выберите опцию: "))
        if option == 1:
            country_manipulator.print_countries()

        elif option == 2:
            try:
                lower_boundary = float(input("Введите нижнюю границу: "))
                upper_boundary = float(input("Введите верхнюю границу: "))
                result = country_manipulator.filter_by_area(lower_boundary, upper_boundary)
                if len(result) == 0:
                    print("Ничего не найдено")
                else:
                    for country in result:
                        print(country)
            except ValueError:
                print("Пожалуйста, введите числа")

        elif option == 3:
            try:
                lower_boundary = int(input("Введите нижнюю границу: "))
                upper_boundary = int(input("Введите верхнюю границу: "))
                result = country_manipulator.filter_by_population(lower_boundary, upper_boundary)
                if len(result) == 0:
                    print("Ничего не найдено")
                else:
                    for country in result:
                        print(country)
            except ValueError:
                print("Пожалуйста, введите числа")

        elif option == 4:
            return 0
        else:
            return -1



