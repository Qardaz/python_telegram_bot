import json
import os


def statistics_output_func():
    statistics_dir_path = os.path.abspath('statistics')
    statistics_json_path = os.path.join(statistics_dir_path, 'request_statistics.json')

    with open(statistics_json_path, 'r', encoding='utf-8') as file:
        input_dict = json.load(file)
        sorted_dict = dict(sorted(input_dict.items(), key=lambda x: x[1], reverse=True))
        output_message = ''
        for key, value in sorted_dict.items():
            output_message += f'{key}: {value}\n'
        print(output_message)


statistics_output_func()
