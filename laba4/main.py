from Triangle import Triangle
import Country
import Transport
from Cinema import Cinema,CinemaManager

if __name__ == "__main__":
    while True:
        try:
            option = int(input("Введите номер задания (0 для выхода): "))

            if option == 1:
                a = float(input('Введите длину первой стороны: '))
                b = float(input('Введите длину второй стороны: '))
                c = float(input('Введите длину третьей стороны: '))
                try:
                    triangle = Triangle(a,b,c)
                except ValueError as e:
                    print(e.args[0])
                    continue

                print(f"Периметр треугольника: {triangle.get_perimeter()}")
                print(f"Площадь треугольника: {triangle.get_area()}")

            elif option == 2:
                Country.select_option()

            elif option == 3:
                Transport.select_option()

            elif option == 4:
                cinema = Cinema.create_sample_cinema()
                cinema_manager = CinemaManager(cinema)
                cinema_manager.run()
            elif option == 0:
                break
            else:
                print("Неверная опция, пожалуйста повторите ваш выбор")
        except ValueError as e:
            print(e.args[0])