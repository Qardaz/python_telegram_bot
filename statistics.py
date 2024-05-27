import json


def statistics_output_func():
    with open('request_statistics.json', 'r', encoding='utf-8') as file:
        input_dict = json.load(file)
        sorted_dict = dict(sorted(input_dict.items(), key=lambda x: x[1], reverse=True))
        output_message = ''
        for key, value in sorted_dict.items():
            output_message += f'{key}: {value}\n'
        print(output_message)


statistics_output_func()
