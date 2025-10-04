def get_chinese_zodiac(year):
    animals = ["Обезьяна", "Петух", "Собака", "Свинья", "Крыса", "Бык",
               "Тигр", "Кролик", "Дракон", "Змея", "Лошадь", "Коза"]
    return animals[year % 12]


def get_chinese_element(year):
    elements = ["Металл", "Вода", "Дерево", "Огонь", "Земля"]
    return elements[(year // 2) % 5]


def is_valid_year(year_str):
    if not year_str.isdigit():
        return False
    year = int(year_str)
    return year > 0

def enable():
    while True:
        year = input("Введите год: ")
        if year == '0': return;
        else:
            if is_valid_year(year):
                year = int(year)
                print(f"Введенный вами год имеет следующие атрибуты: [{get_chinese_zodiac(year)}][{get_chinese_element(year)}]")
            else:
                print("Введенный год неверен")