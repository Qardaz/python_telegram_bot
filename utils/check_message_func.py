def check_message_func(message):
    if not message.isdigit():
        return False
    elif int(message) == 0:
        return False
    return True
