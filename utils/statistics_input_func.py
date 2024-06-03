import json


def statistics_input_func(message):
    with open('statistics/request_statistics.json', 'r', encoding='utf-8') as file:
        new_dict = json.load(file)
        if message not in new_dict:
            new_dict[message] = 0
        new_dict[f'{message}'] += 1

    with open('statistics/request_statistics.json', 'w', encoding='utf-8') as file:
        json.dump(new_dict, file, indent=4, ensure_ascii=False)
