import json
from abc import ABC, abstractmethod
from datetime import timedelta


class TransportVehicle(ABC):

    def __init__(self, name, speed, cost_per_km):
        self.name = name
        self.speed = speed  # км/ч
        self.cost_per_km = cost_per_km  # стоимость за км

    @abstractmethod
    def movement_method(self):
        pass


class Airplane(TransportVehicle):

    def __init__(self):
        super().__init__("Самолет", 800, 5.0)  # 800 км/ч, 5 руб/км

    def movement_method(self):
        return "Передвижение по воздуху с использованием реактивных двигателей"


class Train(TransportVehicle):

    def __init__(self):
        super().__init__("Поезд", 120, 2.0)  # 120 км/ч, 2 руб/км

    def movement_method(self):
        return "Передвижение по рельсовым путям с использованием электрической тяги"


class Car(TransportVehicle):

    def __init__(self):
        super().__init__("Автомобиль", 90, 4.0)  # 90 км/ч, 4 руб/км

    def movement_method(self):
        return "Передвижение по автомобильным дорогам с использованием ДВС"


class Trip:
    next_id = 1
    def __init__(self, transport: TransportVehicle, distance: int, city_from, city_to) -> None:
        self.transport = transport
        self.distance = distance
        self.city_from = city_from
        self.city_to = city_to
        self.id = Trip.next_id
        Trip.next_id += 1

    def calculate_time(self):
        hours = self.distance / self.transport.speed
        return timedelta(hours=hours)

    def calculate_cost(self):
        return self.distance * self.transport.cost_per_km

    def get_trip_info(self):
        time = self.calculate_time()
        cost = self.calculate_cost()

        return {
            'id': self.id,
            'transport': self.transport.name,
            'from': self.city_from,
            'to': self.city_to,
            'distance': self.distance,
            'time_hours': time.total_seconds() / 3600,
            'time_display': str(time),
            'cost': cost,
            'movement_method': self.transport.movement_method()
        }

    def save_to_file(self, filename):
        trip_info = self.get_trip_info()

        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(trip_info, file, ensure_ascii=False, indent=2)

        print(f"Информация сохранена в файл: {filename}")

    def print_trip_info(self):
        trip_info = self.get_trip_info()
        print(f"  Поездка #{trip_info['id']}:")
        print(f"  Маршрут: {trip_info['from']} → {trip_info['to']}")
        print(f"  Транспорт: {trip_info['transport']}")
        print(f"  Расстояние: {trip_info['distance']} км")
        print(f"  Время в пути: {trip_info['time_display']}")
        print(f"  Стоимость: {trip_info['cost']:.2f} руб.")
        print(f"  Способ передвижения: {trip_info['movement_method']}")


class TripCalculator:

    def __init__(self, trips: list[Trip]) -> None:
        self.trips = trips.copy()

    def add_trip(self, trip: Trip) -> None:
        self.trips.append(trip)

    def find_fastest_trip(self, city_from, city_to):
        available_trips = [trip for trip in self.trips if trip.city_from == city_from and trip.city_to == city_to]
        return min(available_trips, key=lambda trip: trip.calculate_time())

    def find_cheapest_trip(self, city_from, city_to):
        available_trips = [trip for trip in self.trips if trip.city_from == city_from and trip.city_to == city_to]
        return min(available_trips, key=lambda trip: trip.calculate_cost())


    def display_all_trips(self):
        for trip in self.trips:
            trip.print_trip_info()
            print("-" * 40)


def create_sample_trips() -> list[Trip]:
    # Создаем транспортные средства
    airplane = Airplane()
    train = Train()
    car = Car()

    # Создаем поездки
    trips = [
        # Москва - Санкт-Петербург
        Trip(airplane, 650, "Москва", "Санкт-Петербург"),
        Trip(train, 650, "Москва", "Санкт-Петербург"),
        Trip(car, 700, "Москва", "Санкт-Петербург"),

        # Москва - Сочи
        Trip(airplane, 1360, "Москва", "Сочи"),
        Trip(train, 1360, "Москва", "Сочи"),
        Trip(car, 1600, "Москва", "Сочи"),

        # Москва - Екатеринбург
        Trip(airplane, 1400, "Москва", "Екатеринбург"),
        Trip(train, 1800, "Москва", "Екатеринбург"),
        Trip(car, 1800, "Москва", "Екатеринбург"),

        # Санкт-Петербург - Сочи
        Trip(airplane, 2100, "Санкт-Петербург", "Сочи"),
        Trip(train, 2400, "Санкт-Петербург", "Сочи"),

        # Короткие поездки
        Trip(car, 100, "Москва", "Тверь"),
        Trip(train, 167, "Москва", "Тверь"),

        # Международные
        Trip(airplane, 2500, "Москва", "Париж"),
        Trip(airplane, 7500, "Москва", "Токио"),
    ]

    return trips

def select_option():

    trip_calculator = TripCalculator(create_sample_trips())
    while True:
        print("1) Показать все поездки \n"
              "2) Найти самую быструю \n"
              "3) Найти самую дешевую \n"
              "4) Выход")
        option = int(input("Выберите опцию: "))
        if option == 1:
            trip_calculator.display_all_trips()

        elif option == 2:
            city_from = input("Введите город отправления: ")
            city_to = input("Введите город назначения: ")
            result = trip_calculator.find_fastest_trip(city_from, city_to)
            if not result:
                print("Ничего не найдено")
            else:
                result.print_trip_info()
                result.save_to_file("fastest_trip.json")

        elif option == 3:
            city_from = input("Введите город отправления: ")
            city_to = input("Введите город назначения: ")
            result = trip_calculator.find_cheapest_trip(city_from, city_to)
            if not result:
                print("Ничего не найдено")
            else:
                result.print_trip_info()
                result.save_to_file("cheapest_trip.json")

        elif option == 4:
            return 0
        else:
            return -1
