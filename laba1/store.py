def start_store():
    vares =  {
            "Тормозные колодки": ["сталь, фрикционный материал, антикоррозийное покрытие", 2500, 15],
            "Масляный фильтр": ["бумажный фильтрующий элемент, стальной корпус, резиновые уплотнения", 800, 25],
            "Воздушный фильтр": ["специальная бумага, пластиковый корпус, полиуретановый уплотнитель", 1200, 18],
            "Свечи зажигания": ["никелевый сплав, керамический изолятор, медный сердечник", 450, 40],
            "Аккумулятор": ["свинцовые пластины, электролит, пластиковый корпус", 8500, 8],
            "Ремень ГРМ": ["высокопрочная резина, нейлоновый корд, тефлоновое покрытие", 3200, 12],
            "Амортизатор": ["стальной корпус, гидравлическая жидкость, резиновые уплотнения", 4800, 10]
        }
    while 1:
        option = int(input("1. Просмотр описания: название – описание\n"
              "2. Просмотр цены: название – цена.\n"
              "3. Просмотр количества: название – количество.\n"
              "4. Вся информацию\n"
              "5. Покупка\n"
              "6. До свидания\n"
              "Выберите опцию: "))
        if option == 1:
            see_description(vares)
        elif option == 2:
            see_price(vares)
        elif option == 3:
            see_amount(vares)
        elif option == 4:
            see_info(vares)
        elif option == 5:
            sell_item(vares)
        elif option == 6:
            return 1

def see_info(vares: dict): #
    for key, value in vares.items():
        print(key)
        print("Описание: " + str(value[0]))
        print("Цена: " + str(value[1]))
        print("Кол-во: " + str(value[2]))
        print("-" * 20)
def see_description(vares: dict): #
    for key, value in vares.items():
        print(key)
        print("Описание: " + str(value[0]))
        print("-" * 20)
def see_price(vares: dict): #
    for key, value in vares.items():
        print(key)
        print("Цена: " + str(value[1]))
        print("-" * 20)
def see_amount(vares: dict): #
    for key, value in vares.items():
        print(key)
        print("Кол-во: " + str(value[2]))
        print("-" * 20)

def sell_item(vares: dict):
    sell_info = {}
    print("Введите данные о товарах (y - для завершения)")
    while True:
        name = str(input("Введите название товара: "))
        if name == "y":
            break
        if name in vares:
            count = int(input("Введите кол-во для продажи: "))
            if 0 < count <= vares[name][2]:
                vares[name][2] -= count
                profit = vares[name][1] * count
                sell_info[name] = (count, profit)
            else:
                print("Кол-во отрицательное или превышает кол-во на складе")
        else:
            print("Товара с таким названием не найдено")
    if sell_info:
        print("\nПокупка успешно совершена!")
        sum = 0
        for key, value in sell_info.items():
            print("Товар: " + key +
            " Количество: " + str(value[0]) +
            " Стоимость: " + str(value[1]) + "руб.")
            print("Остаток на складе: " + str(vares[key][2]))
            sum += value[1]
        print("Общая стоимость: " + str(sum))
