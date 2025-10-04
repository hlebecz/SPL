def divide(a, b):
    result = 0
    try:
        result = a / b
    except ZeroDivisionError:
        print("Деление на ноль запрещено")
    finally:
        print("Результат должен быть всегда")
        print(result)
