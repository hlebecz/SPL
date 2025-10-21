def write_to_file(filename: str):
    with open("F1.txt", "w", encoding='utf-8') as f1:
        while True:
            phrase = str(input("Введите следующую строку: "))
            if phrase:
                f1.write(phrase + "\n")
            else:
                break

def copy_dig_str(f1: str, f2: str):
    f1 = open(f1, "r", encoding='utf-8')
    f2 = open(f2, "w+", encoding='utf-8')
    for line in f1:
        if line[0].isdigit():
            f2.write(line)
    f2.seek(0)
    result = len(f2.readline().split())
    f1.close()
    f2.close()
    return result
