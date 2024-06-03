import os


def show_my_orders_func(message):
    listfiles = []

    your_orders_message = 'Ваши заказы:\n'
    output_message = ''

    order_dir_path = os.path.abspath('orders')

    for file in os.listdir(order_dir_path):
        if file.startswith(f'{message.from_user.id}'):
            listfiles.append(file)
    for file_name in listfiles:
        file_path = os.path.join(order_dir_path, file_name)
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                output_message += f'{line}\n'
    if output_message != '':
        return your_orders_message + output_message
    else:
        return 'Список Ваших заказов пуст ☹️'
