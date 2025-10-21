import json


def save_revenue_to_json(filename: str):
    firms_data = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) >= 4:
                name = parts[0]
                revenue = float(parts[2])
                costs = float(parts[3])
                firms_data.append({
                    'name': name,
                    'revenue': revenue,
                    'costs': costs
                })

    firms_profit = {}
    total_profit = 0
    profitable_firms_count = 0

    for firm in firms_data:
        profit = firm['revenue'] - firm['costs']
        firms_profit[firm['name']] = profit

        if profit > 0:
            total_profit += profit
            profitable_firms_count += 1

    average_profit = total_profit / profitable_firms_count if profitable_firms_count > 0 else 0

    result_list = [
        firms_profit,
        {"average_profit": round(average_profit, 2)}
    ]

    with open('firms_result.json', 'w', encoding='utf-8') as json_file:
        json.dump(result_list, json_file, ensure_ascii=False, indent=2)

    print("Данные успешно обработаны и сохранены в файл 'firms_result.json'")
    print("Результат:")
    print(result_list)