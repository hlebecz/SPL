import f1_f2_copy
import cinema
import curriculum
from firms import save_revenue_to_json

if __name__ == '__main__':
    while True:
        option = int(input("Введите номер задания (0 для выхода): "))

        if option == 1:
            f1_f2_copy.write_to_file("F1.txt")
            print(f"Данные записаны, число слов в первой строке F2 : {f1_f2_copy.copy_dig_str("F1.txt","F2.txt")}")
        elif option == 2:
            cinema.select_option()
        elif option == 3:
            print("Расписание: ")
            for subject, hours in curriculum.summarise_curriculum("Расписание.txt").items():
                print(f"{subject}: {hours}")
        elif option == 4:
            save_revenue_to_json('firms.txt')
        elif option == 0:
            break
        else:
            print("Неверная опция, пожалуйста повторите ваш выбор")